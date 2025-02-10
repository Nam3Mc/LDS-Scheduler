from django.shortcuts import render
from django.http import HttpResponse

def friend(request):
    return HttpResponse('Friend')