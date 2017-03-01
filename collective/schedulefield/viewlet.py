# -*- coding: utf-8 -*-
"""
collective.schedulefield
------------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone.app.layout.viewlets import common as base
from plone.autoform.view import WidgetsView

import json

from collective.schedulefield.behavior import IScheduledContent


class ScheduledContentViewlet(WidgetsView, base.ViewletBase):
    schema = IScheduledContent

    def update(self):
        if self.can_view is True:
            super(ScheduledContentViewlet, self).update()

    @property
    def has_value(self):
        data = json.loads(getattr(self.context, 'schedule', '{}'))
        for day in data.values():
            if len([v for v in day.values() if v]) > 0:
                return True
        return False

    @property
    def can_view(self):
        return IScheduledContent.providedBy(self.context)
