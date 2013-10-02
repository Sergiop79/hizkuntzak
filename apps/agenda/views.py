from django.views.generic import DetailView, ListView
from .models import Ebentua


class EbentuaDetailView(DetailView):
    model = Ebentua
    template_name = 'agenda/agenda_detail.html'
    context_object_name = 'ebentua'


class EbentuaListView(ListView):
    model = Ebentua
    template_name = 'agenda/agenda_list.html'
    context_object_name = 'ebentuak'
