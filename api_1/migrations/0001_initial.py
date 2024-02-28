# Generated by Django 4.2.7 on 2023-11-21 08:53

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouterNetworkDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routing_protocol', models.CharField(default='eigrp', max_length=5)),
                ('asn_number', models.IntegerField(default=1)),
                ('host', models.CharField(blank=True, max_length=50, null=True)),
                ('ssh_ip_address', models.CharField(blank=True, max_length=12, null=True)),
                ('device_type', models.CharField(default='cisco_ios', max_length=20)),
                ('domain_ssh', models.CharField(default='eigrpteam.com', max_length=225)),
                ('username', models.CharField(default='eigrp_redes', max_length=15)),
                ('password', models.CharField(default='cafe_123@', max_length=15)),
                ('secret', models.CharField(default='cafe_123@', max_length=15)),
                ('router_on_stick', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SwitchNetworkDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, max_length=50, null=True)),
                ('admin_vlan', models.IntegerField(default=99)),
                ('ssh_ip_address', models.CharField(blank=True, max_length=12, null=True)),
                ('device_type', models.CharField(default='cisco_ios', max_length=20)),
                ('domain_ssh', models.CharField(default='eigrpteam.com', max_length=225)),
                ('username', models.CharField(default='eigrp_redes', max_length=15)),
                ('password', models.CharField(default='cafe_123@', max_length=15)),
                ('secret', models.CharField(default='cafe_123@', max_length=15)),
                ('vtp_role', models.CharField(blank=True, max_length=12, null=True)),
                ('vtp_domain_name', models.CharField(default='eigrp_team_vtp', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('network_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
