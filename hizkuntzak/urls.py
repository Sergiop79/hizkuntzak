from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

from apps.albisteak.views import AlbisteaView
from apps.agenda.views import EbentuaDetailView, EbentuaListView
from apps.cal.views import calendar

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hizkuntzak.views.home', name='home'),
    # url(r'^hizkuntzak/', include('hizkuntzak.foo.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += i18n_patterns('',
    url(r'^$', AlbisteaView.as_view(), name='albisteak'),
    url(_(r'^agenda/ebentuak/$'), EbentuaListView.as_view(), name='ebentua-list' ),
    url(_(r'^agenda/ebentua/(?P<pk>\d+)/$'), EbentuaDetailView.as_view(), name='ebentua-detail' ),
    url(_(r'^cal/(?P<year>\d{4})/(?P<month>\d{2})/$'), 'apps.cal.views.calendar', name='calendar')
)
