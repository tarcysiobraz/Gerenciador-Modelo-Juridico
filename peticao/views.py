from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from peticao.forms import PeticaoForm
from peticao.models import Peticao


class PeticaoListView(ListView):
    model = Peticao 
    template_name = 'peticao/pages/home.html'
    success_url = reverse_lazy('peticoes')
    context_object_name = 'peticoes'
    def get_queryset(self):
        query = query = self.request.GET.get("q")
        peticoes = Peticao.objects.all().order_by('-id')
        if query:
            peticoes = Peticao.objects.filter(Q(name__icontains=query) | Q(body__icontains=query)).order_by('-id')
        return peticoes


class PeticaoUpdateView(UpdateView):
    model = Peticao 
    form_class = PeticaoForm
    template_name = 'peticao/pages/peticao.html'
    success_url = reverse_lazy('peticoes')
    

class PeticaoCreateView(CreateView):
    form_class = PeticaoForm
    template_name = 'peticao/pages/peticao_created.html'
    success_url = reverse_lazy('peticoes')

class PeticaoDeleteView(DeleteView):
    model = Peticao
    success_url = reverse_lazy('peticoes')
    template_name = 'peticao/pages/peticao_delete.html'
