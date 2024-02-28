
import re


from rest_framework.views import APIView
from rest_framework.response import Response

from api_1.serializers import SwitchSerializer
from ..models import SwitchNetworkDevice
from ..services.tools import GeneralActions

from netmiko import ConnectHandler


class SwitchRunConfig(APIView):
    def get(self, request, pk):
        switch_data = GeneralActions.filter_switch(pk=pk)
        switch_serializer = SwitchSerializer(switch_data).data
        print(switch_serializer)
        device = {
            'device_type': switch_serializer.get('device_type'),
            'host': switch_serializer.get('ssh_ip_address'),
            'username': switch_serializer.get('username'),
            'password': switch_serializer.get('password')
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
