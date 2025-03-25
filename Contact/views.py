from django.shortcuts import render
from .form import contact_form
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Contactform
from django.contrib import messages
# Create your views here.
class ContactCreateView(CreateView):
    model=Contactform
    form_class=contact_form
    template_name = 'contact.html'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user # کاربر را به فرم ارسال کنید
        return kwargs
    def form_valid(self, form):
        if self.request.user.is_authenticated:
        
            form.instance.name = self.request.user.username # مقدار فیلد نام در مدل را تنظیم کنید
        form.save()  # ذخیره فرم
        messages.success(self.request, "پیام شما با موفقیت ارسال شد.")  # نمایش پیام موفقیت
        return render(self.request, self.template_name, {'form': form})  # رندر مجدد صفحه با فرم
        

class comments(ListView):
    model=Contactform
    template_name='comments.html'
    context_object_name = 'comments'


