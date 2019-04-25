from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from billing.services import BillingService

from billing.models import Order
from .forms import PaymentForm, EditOrderForm
from portal.models import Product

@login_required
def payment(request, product_id):
    page_title = 'Purchase'
    # product = get_object_or_404(Product, pk=product_id)
    # form = PaymentForm()
    context = {
        # 'product': product,
        # 'form': form,
        'page_title': page_title
    }
    #
    # user = request.user
    #
    # if request.method == 'POST':
    #     form = PaymentForm(request.POST)
    #     if form.is_valid():
    #         full_name = request.POST.get('first_name').split(' ', 1)
    #         card_data = {
    #             'description': 'Market Place Payment',
    #             'item_type': 'credit_card',
    #             'data': {
    #                 'number': form.cleaned_data['number'],
    #                 'verification_value': form.cleaned_data['verification_value'],
    #                 'first_name': full_name[0],
    #                 'last_name': full_name[1],
    #                 'month': form.cleaned_data['month'],
    #                 'year': form.cleaned_data['year'],
    #             }
    #         }
    #
    #         context['form'] = form
    #         order = BillingService().charge(user, product, card_data)
    #
    #         if order:
    #             return redirect('item_purchased', order.id)
    #
    #         context['error'] = True

    # return render(request, 'billing/payment.html', context)
    return render(request, '404.html', context)

@login_required
def item_purchased(request, order_id):
    page_title = "Item Purchased"
    # order = get_object_or_404(Order, pk=order_id)
    #
    # if order.user != request.user:
    #     return redirect('home')

    context = {
        # 'order': order,
        'page_title': page_title
    }

    # return render(request, 'billing/billing_item_puchased.html', context)\
    return render(request, '404.html', context)

@login_required
def my_orders(request):
    page_title = 'My Orders'
    # orders = Order.objects.filter(merchant=request.user)

    context = {
        # 'orders': orders,
        'page_title': page_title
    }

    # return render(request, 'billing/my_orders.html', context)
    return render(request, '404.html', context)

@login_required
def sales(request):
    page_title = 'My Sales'
    # orders = Order.objects.filter(merchant=request.user, status='Approved')

    context = {
        # 'orders': orders,
        'page_title': page_title
    }

    # return render(request, 'billing/sales.html', context)
    return render(request, '404.html', context)


@login_required
def change_shipment_status(request, order_id):
    page_title = 'Update Shipment Status'
    # order = get_object_or_404(Order, pk=order_id)
    #
    # if order.user != request.user:
    #     return redirect('home')
    #
    # form = EditOrderForm(instance=order)
    #
    # if request.method == 'POST':
    #     form = EditOrderForm(request.POST)
    #     if form.is_valid():
    #         order.shipment_status = form.cleaned_data['shipment_status']
    #         order.save()
    #         return redirect('billing_sales')

    context = {
        'page_title': page_title,
        # 'form': form,
        # 'order': order
    }

    # return render(request, 'billing/change_shipment_status.html', context)
    return render(request, '404.html', context)
