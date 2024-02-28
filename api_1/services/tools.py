from rest_framework.response import Response
from api_1.models import SwitchNetworkDevice, RouterNetworkDevice


class GeneralActions:
    @classmethod
    def filter_switch(cls, pk):
        try:
            object_found = SwitchNetworkDevice.objects.filter(pk=pk).first()
        except SwitchNetworkDevice.DoesNotExist:
            return Response({"Error": "Object not found"})
        return object_found

    @classmethod
    def filter_router(cls, pk):
        try:
            object_found = RouterNetworkDevice.objects.filter(pk=pk).first()
        except RouterNetworkDevice.DoesNotExist:
            return Response({"Error": "Object not found"})
        return object_found
