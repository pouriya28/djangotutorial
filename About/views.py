from django.shortcuts import render,redirect
from django.views.generic import TemplateView

# Create your views here.
class about(TemplateView):
    
    template_name="about.html"
    def get(self, request, *args, **kwargs):
        return redirect('fullpage#section2')
    


class more(TemplateView):
    template_name='more.html'