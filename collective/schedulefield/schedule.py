# -*- coding: utf-8 -*-

import json
from datetime import time

from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implements
from zope.schema.interfaces import IDict
from zope.schema.interfaces import IFromUnicode
from zope.schema.interfaces import WrongContainedType

from z3c.form.interfaces import IFormLayer
from z3c.form.interfaces import IFieldWidget

from z3c.form.widget import FieldWidget
from z3c.form.widget import Widget
from z3c.form.browser.widget import HTMLInputWidget

from collective.schedulefield import _


class ISchedule(IDict):
    """
    """


class Schedule(schema.Dict):
    implements(ISchedule, IFromUnicode)

    def fromUnicode(self, value):
        """
        """
        self.validate(value)
        return value

    def validate(self, value):
        value = json.loads(value)
        for day in value:
            for day_section in value[day]:
                error = self._validate_format(value[day][day_section])
                if error:
                    raise WrongContainedType(error, self.__name__)

    def _validate_format(self, data):
        """
        12:10 > time(12, 10)
        """
        if not data:
            return None
        hour, minute = data.split(':')
        try:
            time(int(hour), int(minute))
        except ValueError:
            return _(u'Not a valid time format.')

        return None


class ScheduleWidget(HTMLInputWidget, Widget):
    implements(ISchedule)
    """Schedule widget implementation."""

    klass = u'schedule-widget'
    css = u'schedule'
    value = u''
    size = 10
    maxlength = 10

    @property
    def days(self):
        return (('monday', _('Monday')),
                ('tuesday', _('Tuesday')),
                ('wednesday', _('Wednesday')),
                ('thursday', _('Thursday')),
                ('friday', _('Friday')),
                ('saturday', _('Saturday')),
                ('sunday', _('Sunday')))

    @property
    def day_sections(self):
        return ('morningstart',
                'morningend',
                'afternoonstart',
                'afternoonend')

    def update(self):
        super(ScheduleWidget, self).update()
        self.value = json.loads(self.value)

    def extract(self):
        datas = {}
        for key, name in self.days:
            datas[key] = {}
            for day_section in self.day_sections:
                data = self.request.get('{0}.{1}.{2}'.format(self.name, key, day_section), None)
                datas[key][day_section] = self._format(data)

        return json.dumps(datas)

    @staticmethod
    def _format(data):
        if data == '__:__':
            return None
        return data


@adapter(ISchedule, IFormLayer)
@implementer(IFieldWidget)
def ScheduleFieldWidget(field, request):
    """IFieldWidget factory for cheduleWidget."""
    return FieldWidget(field, ScheduleWidget(request))
