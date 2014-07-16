# -*- coding: utf-8 -*-

from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implements
from zope.schema.interfaces import IDict

from z3c.form.interfaces import IFormLayer
from z3c.form.interfaces import IFieldWidget

from z3c.form.widget import FieldWidget
from z3c.form.widget import SequenceWidget


class ISchedule(IDict):
    """
    """


class Schedule(schema.Dict):
    implements(ISchedule)


class Terms(object):

    def getTerm(self, value):
        return type('obj', (object, ), {'token': value})

    def getValue(self, token):
        return token


class ScheduleWidget(SequenceWidget):
    implements(ISchedule)
    """Schedule widget implementation."""

    klass = u'schedule-widget'
    css = u'schedule'
    value = u''

    def updateTerms(self):
        self.terms = Terms()
        return self.terms


@adapter(ISchedule, IFormLayer)
@implementer(IFieldWidget)
def ScheduleFieldWidget(field, request):
    """IFieldWidget factory for cheduleWidget."""
    return FieldWidget(field, ScheduleWidget(request))
