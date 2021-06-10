from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Code
from django.urls import reverse_lazy

# Create your views here.

class CodeListView(ListView):
    model = Code
    template_name = 'code_list.html' 

class CodeDetailView(DetailView):
    model = Code
    template_name = 'code_detail.html'

class CodeEditView(UpdateView):
    model = Code
    template_name = 'code_edit.html'
    fields = ('title', 'body',)

class CodeDeleteView(DeleteView):
    model = Code
    template_name = 'code_delete.html'
    success_url = reverse_lazy('code_list')

class CodeCreateView(CreateView):
    model = Code
    template_name = 'code_post.html'
    fields = ('title', 'body', 'author',)