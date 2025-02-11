from .models import Ward
from rest_framework import status
from rest_framework.response import Response
from .serializer import WardSerializer

def getWards():
    wards = Ward.objects.all()
    serializer = WardSerializer(wards, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def getWard(ward_id):
    pass

def createWard(request):
    serializer = WardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def updateWard(ward_id, ward):
    pass

def deleteWard(ward_id):
    pass
