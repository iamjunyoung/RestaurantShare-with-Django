from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

def sendEmail(request):
    #return HttpResponse("sendEmail")
    return HttpResponseRedirect(reverse('index'))

