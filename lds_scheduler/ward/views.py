from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from django.contrib.auth.decorators import login_required
from .services import getWards, getWard, createWard, updateWard, deleteWard


class WardsView(APIView):

    def get(self, request):
        wards = getWards()
        return wards

    @login_required
    def post(self, request):
        newWard = createWard(request)
        return newWard
    
class WardById(APIView):

    def get(self, request, ward_id):
        ward = getWard(request, ward_id)
        return ward
    
    @authentication_classes([])
    @permission_classes([])
    @login_required
    def put(self, request, ward_id):
        updatedWard = updateWard(request, ward_id)
        return updatedWard
    
    # @authentication_classes([])
    # @permission_classes([])
    @login_required
    def delete(self, request, ward_id):
        deletedWard = deleteWard(request, ward_id)
        return deletedWard