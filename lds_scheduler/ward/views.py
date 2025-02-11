from rest_framework.views import APIView
from .services import getWards, getWard, createWard, updateWard, deleteWard


class WardsView(APIView):

    def get(self, request):
        wards = getWards()
        return wards
    def post(self, request):
        newWard = createWard(request)
        return newWard