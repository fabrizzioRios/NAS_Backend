
from .models import SwitchNetworkDevice, RouterNetworkDevice, User

from rest_framework.serializers import ModelSerializer


class SwitchSerializer(ModelSerializer):
    class Meta:
        model = SwitchNetworkDevice
        fields = '__all__'


class RouterSerializer(ModelSerializer):
    class Meta:
        model = RouterNetworkDevice
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
