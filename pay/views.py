from django.shortcuts import render

# Create your views here.


def pay(request):
    return render(request, 'pay/pay.html')


def payok(request):
    return render(request, 'pay/payok.html')