import json
import ipaddress

deviceJSON = '{"Version": "15.6", "locationN": "500 Northridge", "role": "Access", "upTime": "12:10:53.49", "hostname": "ATL-3650-1", "macAddress": "39:58:1f:9e:38:c1", "series": "Cisco Catalyst 3650 Series Switches", "lastUpdated": "2017-09-21 13:12:46", "bootDateTime": "2016-10-27 05:24:53", "interfaceCount": "24", "lineCardCount": "1", "managementIpAddress": "192.168.10.10", "interfaces": {"interface": [{"GigabitEthernet0": {"ipv4": "100.100.100.1"}}, {"GigabitEthernet1": {"ipv4": "10.10.10.2"}}]}}'

json_data = json.loads(deviceJSON)

#Get Interface Ip addresses
interface_gig0 = json_data['interfaces']['interface'][0]["GigabitEthernet0"]["ipv4"]
interface_gig1 = json_data['interfaces']['interface'][1]["GigabitEthernet1"]["ipv4"]

ipaddress_gig0 = ipaddress.ip_address(interface_gig0)
ipaddress_gig1 = ipaddress.ip_address(interface_gig1)

#check if IP is RFC 1928

if ipaddress_gig0 in ipaddress.ip_network('10.0.0.0/8'):
    print('GigabitEthernet0 has an IP address of',interface_gig0 , "it is a Private adddress")
elif ipaddress_gig0 in ipaddress.ip_network('172.16.0.0/12'):
    print('GigabitEthernet0 has an IP address of',interface_gig0 , "it is a Private adddress")
elif ipaddress_gig0 in ipaddress.ip_network('192.168.0.0/16'):
    print('GigabitEthernet0 has an IP address of',interface_gig0 , "it is a Private adddress")
else:
    print('GigabitEthernet0 has an IP address of',interface_gig0 , "it is not a Private adddress")

if ipaddress_gig1 in ipaddress.ip_network('10.0.0.0/8'):
    print('GigabitEthernet1 has an IP address of',interface_gig1 , "it is a Private adddress")
elif ipaddress_gig1 in ipaddress.ip_network('172.16.0.0/12'):
    print('GigabitEthernet1 has an IP address of',interface_gig1 , "it is a Private adddress")
elif ipaddress_gig1 in ipaddress.ip_network('192.168.0.0/16'):
    print('GigabitEthernet1 has an IP address of',interface_gig1 , "it is a Private adddress")
else:
    print('GigabitEthernet1 has an IP address of',interface_gig1 , "it is not a Private adddress")


#debugging
#print(interface_gig0)
#print(interface_gig1)





    
    
