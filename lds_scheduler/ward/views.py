from django.shortcuts import render
from django.http import HttpResponse

def ward(request):
    return HttpResponse('Wards')