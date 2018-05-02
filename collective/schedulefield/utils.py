# encoding: utf-8
from collective.schedulefield.behavior import IMultiScheduledContent
from collective.schedulefield.behavior import IExceptionalClosureContent


def get_schedule_by_date(context, date):
    """get_schedule_by_date

    :param context: IMultiScheduledContent
    :param date: Date
    """
    if IExceptionalClosureContent.providedBy(context):
        dates = getattr(context, 'exceptional_closure', None) or []
        for d in dates:
            if date == d.date:
                return {'title': d.title,
                        'morningstart': None,
                        'morningend': None,
                        'afternoonstart': None,
                        'afternoonend': None}
    if IMultiScheduledContent.providedBy(context):
        multi_schedule = getattr(context, 'multi_schedule', None) or []
        for i in multi_schedule:
            schedule = i.schedule
            dates = i.dates or []
            for d in dates:
                if d.start_date <= date <= d.end_date:
                    schedule = dict(schedule.get(date.strftime("%A").lower()))
                    schedule.pop('comment')
                    schedule.update({'title': i.title})
                    return schedule
        schedule = getattr(context, 'schedule', None)
        if schedule:
            schedule = dict(schedule.get(date.strftime("%A").lower()))
            schedule.pop('comment')
            schedule.update({'title': None})
        return schedule
