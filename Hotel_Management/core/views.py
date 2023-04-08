from django.shortcuts import render

# Create your views here.

def waiter(request):
    return render(request, 'waiter.html')

def manager(request):
    return render(request, 'manager.html')

def bill_desk(request):
    return render(request, 'bill_desk.html')