# encoding: utf-8
from collective.schedulefield.behavior import IMultiScheduledContent


def get_schedule_by_date(context, date):
    """get_schedule_by_date

    :param context: IMultiScheduledContent
    :param date: Date
    """
    if IMultiScheduledContent.providedBy(context):
        multi_schedule = getattr(context, 'multi_schedule', None) or []
        for i in multi_schedule:
            schedule = i.schedule
            if i.start_date <= date <= i.end_date:
                return schedule
        return getattr(context, 'schedule', None)
