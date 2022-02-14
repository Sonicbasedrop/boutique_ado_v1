from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe__public_key': 'pk_test_51KRELIIkA8ERQ8dp2tdsHrSePo1ZJLxi6kettukRoMINh3Dzanzi1abdumEARHWSkERCaVWA0Vg1eICoctjqwR2T00Jdnsdvqq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
