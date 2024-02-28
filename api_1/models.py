from django.contrib.auth.models import AbstractUser
from django.db import models


class SwitchNetworkDevice(models.Model):
    host = models.CharField(max_length=50, blank=True, null=True)
    admin_vlan = models.IntegerField(default=99)
    ssh_ip_address = models.CharField(max_length=16, blank=True, null=True)
    device_type = models.CharField(max_length=20, blank=True, null=True)
    domain_ssh = models.CharField(max_length=225, blank=True, null=True)
    username = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=15, blank=True, null=True)
    secret = models.CharField(max_length=15, blank=True, null=True)
    vtp_role = models.CharField(max_length=12, blank=True, null=True)
    vtp_domain_name = models.CharField(max_length=15, blank=True, null=True)


class RouterNetworkDevice(models.Model):
    routing_protocol = models.CharField(max_length=5, blank=True, null=True)
    asn_number = models.IntegerField(default=1)
    host = models.CharField(max_length=50, blank=True, null=True)
    ssh_ip_address = models.CharField(max_length=16, blank=True, null=True)
    device_type = models.CharField(max_length=20, blank=True, null=True)
    domain_ssh = models.CharField(max_length=225, blank=True, null=True)
    username = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=15, blank=True, null=True)
    secret = models.CharField(max_length=15, blank=True, null=True)
    router_on_stick = models.BooleanField(default=False)


class User(AbstractUser):
    network_admin = models.BooleanField(default=False)
