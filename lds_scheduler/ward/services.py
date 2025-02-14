from .models import Ward
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
from .serializer import WardSerializer

def getWards():
    wards = Ward.objects.all()
    serializer = WardSerializer(wards, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def getWard(request, ward_id):
    ward = get_object_or_404(Ward, pk=ward_id)
    serializer = WardSerializer(ward)
    return Response(serializer.data, status=status.HTTP_200_OK)

def createWard(request):
    ward_unit = request.data.get('unitId')
    ward = Ward.objects.filter(unitId=ward_unit)

    if ward:
        return Response({'Error', 'This ward is already added'}, status=status.HTTP_409_CONFLICT)

    serializer = WardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def updateWard(request, ward_id):
    ward = get_object_or_404(Ward, pk=ward_id)
    serializer = WardSerializer(ward, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteWard(reuqest, ward_id):
    ward = get_object_or_404(Ward, pk=ward_id)
    if ward:
        ward.delete()
        return Response( {'message': 'Ward deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response( {'message': 'Ward not found'}, status=status.HTTP_404_NOT_FOUND)