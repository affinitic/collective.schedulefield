# -*- coding: utf-8 -*-
"""
collective.schedulefield
------------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from collective.schedulefield.behavior import IMultiScheduledContent
from collective.schedulefield.behavior import IScheduledContent
from plone.app.layout.viewlets import common as base
from plone.autoform.view import WidgetsView
from datetime import date
from datetime import timedelta
from collective.schedulefield.utils import get_schedule_by_date


TIMEDELTA = 14


class ScheduledContentViewlet(WidgetsView, base.ViewletBase):
    schema = IScheduledContent

    def update(self):
        if self.can_view is True:
            super(ScheduledContentViewlet, self).update()

    @property
    def has_value(self):
        schedule = getattr(self.context, 'schedule', None)
        if schedule:
            for day in schedule.values():
                if len([v for v in day.values() if v]) > 0:
                    return True
        return False

    @property
    def can_view(self):
        return IScheduledContent.providedBy(self.context)


class MultiScheduledContentViewlet(ScheduledContentViewlet):
    schema = IMultiScheduledContent

    @property
    def has_value(self):
        multi_schedule = getattr(self.context, 'multi_schedule', None) or []
        for i in multi_schedule:
            if i.start_date <= date.today() <= i.end_date:
                return False
        return super(MultiScheduledContentViewlet, self).has_value

    @property
    def has_multivalue(self):
        multi_schedule = getattr(self.context, 'multi_schedule', None) or []
        for i in multi_schedule:
            schedule = i.schedule
            if schedule:
                for day in schedule.values():
                    if len([v for v in day.values() if v]) > 0:
                        return True
        return False

    @property
    def get_multischedule(self):
        widgets = []
        multi_schedule = self.w.get('multi_schedule').widgets
        for i in multi_schedule:
            schedule = i._value['schedule']
            if schedule:
                for day in schedule.values():
                    if len([v for v in day.values() if v]) > 0:
                        if i._value['start_date'] - timedelta(days=TIMEDELTA) <= date.today() <= i._value['end_date']:
                            widgets.append(i)
        return widgets

    @property
    def can_view(self):
        from datetime import date
        get_schedule_by_date(self.context, date.today())
        return IMultiScheduledContent.providedBy(self.context)
