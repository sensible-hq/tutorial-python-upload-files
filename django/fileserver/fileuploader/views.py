from django.shortcuts import render

# Create your views here.

# add the imports to the top
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import FileUpload

class FileUploadView(CreateView):
    model = FileUpload
    fields = ['file', ]
    success_url = reverse_lazy('fileupload')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = FileUpload.objects.all()
        return context

