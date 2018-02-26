# -*- coding: utf-8 -*-
"""
collective.schedulefield
------------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform.view import WidgetsView
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel.directives import fieldset
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider

from collective.schedulefield import _
from collective.schedulefield.schedule import Schedule

from z3c.form.object import registerFactoryAdapter
from zope.schema import Date
from zope.schema import List
from zope.schema import Object
from zope.schema import Text
from zope.schema.fieldproperty import FieldProperty


@provider(IFormFieldProvider)
class IScheduledContent(Interface):

    fieldset(
        'schedule',
        label=_('Schedule'),
        fields=['schedule'],
    )

    schedule = Schedule(
        title=_(u'Schedule'),
        required=False,
    )


@implementer(IScheduledContent)
@adapter(IDexterityContent)
class ScheduledContent(object):

    def __init__(self, context):
        self.context = context


class WidgetView(WidgetsView):
    schema = IScheduledContent


class IScheduledWithTitle(Interface):
    """ Helper schema for min and max fields """

    title = Text(
        title=_(u'Title'),
        required=False
    )

    start_date = Date(
        title=_(u'Start date'),
        required=False
    )

    end_date = Date(
        title=_(u'End date'),
        required=False
    )

    schedule = Schedule(
        title=_(u'Schedule'),
        required=False,
    )


@implementer(IScheduledWithTitle)
class ScheduledWithTitle(object):
    """ScheduledWithTitle"""
    title = FieldProperty(IScheduledWithTitle['title'])
    start_date = FieldProperty(IScheduledWithTitle['start_date'])
    end_date = FieldProperty(IScheduledWithTitle['end_date'])
    schedule = FieldProperty(IScheduledWithTitle['schedule'])


registerFactoryAdapter(IScheduledWithTitle, ScheduledWithTitle)


@provider(IFormFieldProvider)
class IMultiScheduledContent(Interface):

    fieldset(
        'multischedule',
        label=_('Multi Schedule'),
        fields=['schedule', 'multi_schedule'],
    )

    schedule = Schedule(
        title=_(u'Schedule'),
        required=False,
    )

    multi_schedule = List(
        title=_(u'Multi Schedule'),
        value_type=Object(__name__='MultiSchedule', schema=IScheduledWithTitle, required=False),
        required=False,
    )


@implementer(IMultiScheduledContent)
@adapter(IDexterityContent)
class MultiScheduledContent(ScheduledContent):
    pass
