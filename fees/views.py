from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Fee, Payment

# Create your views here.


def fee_list(request):
    fees = Fee.objects.all()
    return render(request, 'fee_list.html', {'fees': fees})

def fee_detail(request, fee_id):
    fee = get_object_or_404(Fee, id=fee_id)
    return render(request, 'fee_detail.html', {'fee': fee})

def make_payment(request, fee_id):
    fee = get_object_or_404(Fee, id=fee_id)
    if request.method == 'POST':
        amount_paid = request.POST['amount_paid']
        payment = Payment(fee=fee, amount_paid=amount_paid)
        payment.save()
        fee.paid = True
        fee.paid_date = payment.payment_date
        fee.save()
        return HttpResponse('Payment successful')
    return render(request, 'make_payment.html', {'fee': fee})