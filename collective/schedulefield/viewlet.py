# -*- coding: utf-8 -*-
"""
collective.schedulefield
------------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone.app.layout.viewlets import common as base
from plone.autoform.view import WidgetsView

from collective.schedulefield.behavior import IScheduledContent


class ScheduledContentViewlet(WidgetsView, base.ViewletBase):
    schema = IScheduledContent

    def can_view(self):
        return IScheduledContent.providedBy(self.context)
