from django.shortcuts import render
from django.http import HttpResponse

def invitation(request):
    return HttpResponse('Invitation')