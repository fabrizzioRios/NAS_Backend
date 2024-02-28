import time
import asyncio

from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException


async def test():
    ssh_connections = []
    device_config_order = [
        {
            'host': 'SWITCH_3',
            'ip': '192.168.0.148',
            'config': [
                # 'conf t\n',
                'line con 0',
                'password cafe_123@',
                'login',
                'exit',
                'enable secret cafe_123@',
                'service password-encryption',
                'banner motd cEIGRP Team - Personal Access Onlyc',
                'vtp mode server',
                'vtp domain eigrpvtp.com',
                'vtp password cafe_123@',
                'interface range fa0/1',
                'switchport mode trunk',
                'switchport trunk allowed vlan 10,20,30,40,99',
                'no shut',
                'interface range fa0/2-3',
                'shutdown',
                'channel-group 1 mode desirable',
                'switchport trunk allowed vlan 10,20,30,40,99',
                'no shut',
                'interface po1',
                'switchport mode trunk',
                'interface fa0/4',
                'switchport mode access',
                'switchport access vlan 20',
                'interface fa0/5',
                'switchport mode access',
                'switchport access vlan 10',
                'interface fa0/6',
                'switchport mode access',
                'switchport access vlan 99'
                'end'
            ]
        },
        {
            'host': 'SWITCH_2',
            'ip': '192.168.0.147',
            'config': [
                # 'conf t',
                'line con 0',
                'password cafe_123@',
                'login',
                'exit',
                'enable secret cafe_123@',
                'service password-encryption',
                'banner motd cEIGRP Team - Personal Access Onlyc',
                'vlan 10',
                'name Architecture',
                'vlan 20',
                'name Cibersecurity',
                'vlan 30',
                'name WebDeveloping',
                'vlan 40',
                'name Automation',
                'vlan 99',
                'name Administration',
                'interface range fa0/1-3',
                'switchport mode trunk',
                'switchport trunk allowed vlan 10,20,30,40,99',
                'vtp mode server',
                'vtp domain eigrpvtp.com',
                'vtp password cafe_123@',
                'end'
            ]
        },
        {
            'host': 'SWITCH_1',
            'ip': '192.168.0.146',
            'config': [
                'line con 0',
                'password cafe_123@',
                'login',
                'exit',
                'enable secret cafe_123@',
                'service password-encryption',
                'banner motd cEIGRP Team - Personal Access Onlyc',
                'vtp mode server',
                'vtp domain eigrpvtp.com',
                'vtp password cafe_123@',
                'interface range fa0/1',
                'switchport mode trunk',
                'switchport trunk allowed vlan 10,20,30,40,99',
                'interface range fa0/2-3',
                'shutdown',
                'channel-group 1 mode desirable',
                'switchport trunk allowed vlan 10,20,30,40,99',
                'no shutdown',
                'interface po1',
                'switchport mode trunk',
                'interface fa0/4',
                'switchport mode access',
                'switchport access vlan 30',
                'interface fa0/5',
                'switchport mode access',
                'switchport access vlan 40',
                'end'
            ]
        },
        {
            'host': 'ROUTER_2',
            'ip': '192.168.0.145',
            'config': [
                # 'conf t',
                'line con 0',
                'password cafe_123@',
                'login',
                'exit',
                'enable secret cafe_123@',
                'service password-encryption',
                'banner motd cEIGRP Team - Personal Access Onlyc',
                'router eigrp 1',
                'network 192.168.0.4 0.0.0.3',
                'no auto-summary',
                'network 192.168.0.12 0.0.0.3',
                'no auto-summary',
                'network 192.168.0.80 0.0.0.15',
                'no auto-summary',
                'network 192.168.0.96 0.0.0.15',
                'no auto-summary',
                'network 192.168.0.112 0.0.0.15',
                'no auto-summary',
                'network 192.168.0.128 0.0.0.15',
                'no auto-summary',
                'network 192.168.0.144 0.0.0.15',
                'no auto-summary',
                'passive-interface fa0/0',
                'ip dhcp pool vlan10',
                'network 192.168.0.80 255.255.255.240',
                'ip dhcp pool vlan20',
                'network 192.168.0.96 255.255.255.240',
                'ip dhcp pool vlan30',
                'network 192.168.0.112 255.255.255.240',
                'ip dhcp pool vlan40',
                'network 192.168.0.128 255.255.255.240',
                'end'
            ]
        },
        {
            'host': 'ROUTER_3',
            'ip': '192.168.0.13',
            'config': [
                # 'conf t\n',
                'line con 0',
                'password cafe_123@',
                'login',
                'exit',
                'enable secret cafe_123@',
                'service password-encryption',
                'banner motd cEIGRP Team - Personal Access Onlyc',
                'router eigrp 1',
                'network 192.168.0.8 0.0.0.3',
                'no auto-summary',
                'network 192.168.0.12 0.0.0.3',
                'no auto-summary',
                'end'
            ]
        },
        {
            'host': 'ROUTER_1',
            'ip': '192.168.0.6',
            'config': [
                # 'conf t',
                'line con 0',
                'password cafe_123@',
                'login',
                'exit',
                'enable secret cafe_123@',
                'service password-encryption',
                'banner motd cEIGRP Team - Personal Access Onlyc',
                'router eigrp 1',
                'network 192.168.0.0 0.0.0.3',
                'no auto-summary',
                'network 192.168.0.4 0.0.0.3',
                'no auto-summary',
                'network 192.168.0.8 0.0.0.63',
                'no auto-summary',
                'end'
            ]
        },
        # {
        #     'host': 'ROUTER_D',
        #     'ip': '192.168.0.1'
        # },

    ]

    for element in device_config_order:
        device = {
            'device_type': 'cisco_ios',
            'ip': element.get('ip'),
            'username': 'eigrp_redes',
            'password': 'cafe_123@'
        }
        print(ConnectHandler(**device))
        connection = await ssh_connection(device)
        print(connection)
        # if connection:
        #     print(await config_commands(connection, element.get('config')))


async def ssh_connection(device):
    await asyncio.sleep(10)
    return ConnectHandler(**device)


# async def config_commands(connection, command_list):
#     await asyncio.sleep(15)
#     return connection.send_config_set(command_list)


# Run the event loop to execute the async function
asyncio.run(test())
