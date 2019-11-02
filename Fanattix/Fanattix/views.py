from django.http import HttpResponse
from django.shortcuts import render



def homepage(request):
    return render(request,'ticket-purchase.component.html')



def about(request):

    return render(request,'home.html')