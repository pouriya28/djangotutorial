from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Product
from django.contrib import messages
from django.core.exceptions import PermissionDenied

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart.quantity += 1
        cart.save()

    return redirect('Cart:cart_view')


def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart_view.html', {'cart_items': cart_items, 'total_price': total_price})



def remove_item(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)
    # بررسی اینکه آیتم متعلق به کاربر فعلی است
    if item.user != request.user:
        raise PermissionDenied  # اگر کاربر مجاز نباشد، خطای 403 ایجاد می‌شود

    item.delete()  # حذف آیتم از دیتابیس
    messages.success(request, 'آیتم با موفقیت حذف شد.')  # نمایش پیام موفقیت
    return redirect('Cart:cart_view')  # بازگشت به صفحه‌ی سبد خرید
def decrease_quantity(request, item_id):
    item = get_object_or_404(Cart, id=item_id)

    # بررسی اینکه آیتم متعلق به کاربر فعلی است
    if item.user != request.user:
        raise PermissionDenied  # اگر کاربر مجاز نباشد، خطای 403 ایجاد می‌شود

    # کاهش تعداد محصول
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
        messages.success(request, 'تعداد محصول با موفقیت کاهش یافت.')
    else:
        # حذف آیتم اگر تعداد آن صفر شود
        item.delete()
        messages.success(request, 'آیتم با موفقیت از سبد خرید حذف شد.')

    return redirect('Cart:cart_view') 

def update_cart(request):
    if request.method == 'POST':
        for item in request.POST:
            if item.startswith('quantity_'):
                cart_id = int(item.split('_')[1])
                quantity = int(request.POST[item])
                cart = get_object_or_404(Cart, id=cart_id)
                if quantity <= 0:
                    remove_item(request, cart_id)  # فراخوانی remove_item با cart_id
                else:
                    cart.quantity = quantity
                    cart.save()
    return redirect('Cart:cart_view')