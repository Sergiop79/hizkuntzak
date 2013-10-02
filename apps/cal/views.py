from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe
from django.template import RequestContext
from django.utils import translation

from apps.agenda.models import Ebentua
from apps.cal.models import EventCalendar
from hizkuntzak import settings


def calendar(request, year, month):
    # Avoid people writing wrong numbers or any program errors
    if int(month) not in range(1, 13):
        return render_to_response('cal/cal_error.html', context_instance=RequestContext(request))

    next_month = int(month) + 1
    prev_month = int(month) - 1

    ebentuak = Ebentua.objects.order_by('data') \
            .filter(data__year=year, data__month=month)

    cur_lang = translation.get_language()
    if cur_lang == 'eu':
        cur_locale = 'eu_ES.UTF-8'
    elif cur_lang == 'es':
        cur_locale = 'es_ES.UTF-8'
    elif cur_lang == 'en':
        cur_locale = 'en_GB.UTF-8'
    # hizkuntzen locale-ak instalatura egon behar dira
    #cur_locale = translation.to_locale(cur_lang) + ' .UTF-8'
    cal = EventCalendar(ebentuak, 0, cur_locale).format_month(int(year), int(month))
    return render_to_response('cal/calendar.html',
            {'calendar': mark_safe(cal),
                'nextmonth': '%02d' % next_month,
                'prevmonth': '%02d' % prev_month},
            context_instance = RequestContext(request))
