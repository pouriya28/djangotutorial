from django.shortcuts import render,redirect
from Products.models import Product
from Contact.form import contact_form

from django.views.generic import ListView
from Contact.models import Contactform
from django.contrib import messages
def fullpage_view(request):
    return render(request, 'fullpage.html')

def fullpage_section(request, section):
    # دریافت محصولات فعال
    products = Product.objects.all().filter(activ=True)  # تصحیح از activ به active
    
    # مدیریت فرم تماس
    form = contact_form(user=request.user)  # مقدار اولیه فرم
    
    if request.method == 'POST':
        # اگر فرم ارسال شده باشد
        form = contact_form(request.POST, user=request.user)
        if form.is_valid():
            contact = form.save(commit=False)
            if request.user.is_authenticated:
                contact.name = request.user.username
            contact.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد.")
            # بعد از ارسال موفق فرم، ریفرش کنیم
            return redirect(request.path)  # به همان صفحه برگردد
    
    context = {
        'section': section,
        'products': products,
        'form': form,
        'comments':Contactform.objects.all()
    }
    return render(request, 'fullpage.html', context)        