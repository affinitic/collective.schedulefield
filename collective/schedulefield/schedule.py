# -*- coding: utf-8 -*-

import json

from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implements
from zope.schema.interfaces import IDict
from zope.schema.interfaces import IFromUnicode

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

    def fromUnicode(self, str):
        """
        """
        self.validate(str)
        return str

    def validate(self, str):
        # XXX valider le type de valeur
        pass


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

    def update(self):
        super(ScheduleWidget, self).update()
        self.value = json.loads(self.value)

    def extract(self):
        # XXX il va y avoir plusieurs champs par jour
        datas = {}
        for key, name in self.days:
            data = self.request.get('{0}.{1}'.format(self.name, key), None)
            datas[key] = data

        return json.dumps(datas)

@adapter(ISchedule, IFormLayer)
@implementer(IFieldWidget)
def ScheduleFieldWidget(field, request):
    """IFieldWidget factory for cheduleWidget."""
    return FieldWidget(field, ScheduleWidget(request))
