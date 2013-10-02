from django.views.generic import ListView
from .models import Albistea


class AlbisteaView(ListView):
    model = Albistea
    queryset = Albistea.objects.all().order_by('-id')
    template_name = 'albisteak/albisteak.html'
    context_object_name = 'albisteak'
