# Generated by Django 4.2.7 on 2023-11-25 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_1', '0003_alter_switchnetworkdevice_ssh_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routernetworkdevice',
            name='device_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='routernetworkdevice',
            name='domain_ssh',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='routernetworkdevice',
            name='password',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='routernetworkdevice',
            name='routing_protocol',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='routernetworkdevice',
            name='secret',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='routernetworkdevice',
            name='username',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='switchnetworkdevice',
            name='device_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='switchnetworkdevice',
            name='domain_ssh',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='switchnetworkdevice',
            name='password',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='switchnetworkdevice',
            name='secret',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='switchnetworkdevice',
            name='username',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='switchnetworkdevice',
            name='vtp_domain_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]