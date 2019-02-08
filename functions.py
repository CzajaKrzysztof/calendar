import ui
import storage
from datetime import datetime


def get_todays_meetings(meetings):
    today_meetings = []
    current_date = get_currnet_date()
    for meeting in meetings:
        meeting_date = join_date(*meeting[:3])
        if current_date == meeting_date:
            today_meetings.append(meeting)

    return today_meetings


def get_currnet_date():
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    current_date = join_date(year, month, day)

    return current_date


def join_date(year, month, day):
    if len(str(month)) < 2:
        month = '0' + str(month)
    if len(str(day)) < 2:
        day = '0' + str(day)

    date = str(year) + str(month) + str(day)

    return date
