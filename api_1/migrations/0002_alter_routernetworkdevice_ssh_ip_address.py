# Generated by Django 4.2.7 on 2023-11-25 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routernetworkdevice',
            name='ssh_ip_address',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
