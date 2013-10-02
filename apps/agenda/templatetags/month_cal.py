from django import template
from datetime import date, timedelta
from apps.agenda,models import Ebentua

register = template.Library()

def get_last_day_of_month(year, month):
    if(month == 12):
        year += 1
        month = 1
    else:
        month += 1

    return date(year, month, 1) - timedelta(1)



