import re

from rest_framework.views import APIView
from rest_framework.response import Response

from netmiko import ConnectHandler

from api_1.serializers import RouterSerializer

from api_1.services.devices import Device
from api_1.services.tools import GeneralActions


class RouterRunConfig(APIView):
    def get(self, request, pk):
        router_data = GeneralActions.filter_router(pk=pk)
        router_serializer = RouterSerializer(router_data).data
        print(router_serializer)
        device = {
            'device_type': router_serializer.get('device_type'),
            'host': router_serializer.get('ssh_ip_address'),
            'username': router_serializer.get('username'),
            'password': router_serializer.get('password')
        }
        print(device)
        device_connection = ConnectHandler(**device)
        print(device_connection)
        device_connection.enable()
        cdp_neigh = device_connection.send_command('sh cdp neigh')
        data_from_cdp = re.findall(r"(\bSWITCH_\d\.eigrpteam\.com.*?|\bFas 0/\d|ROUTER_\d\.eigrpteam\.com)", cdp_neigh)
        test_list = [(data_from_cdp[i], data_from_cdp[i + 1]) for i in range(0, len(data_from_cdp), 3)]
        print(data_from_cdp)
        print(test_list)
        device_connection.disconnect()
        return Response({"Success": test_list})
