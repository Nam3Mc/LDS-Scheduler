from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Ward

def ward(request):
    wardsList = list(Ward.objects.all().values())
    return JsonResponse(wardsList, safe=False)

def add(request):
    newWard = Ward(address='Atalaya', unitId='123456', )
    newWard.save()
    return HttpResponse('Ward added')