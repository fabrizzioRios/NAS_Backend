
from rest_framework import viewsets
from .models import SwitchNetworkDevice, RouterNetworkDevice, User
from .serializers import SwitchSerializer, RouterSerializer, UserSerializer


class SwitchViewSets(viewsets.ModelViewSet):
    queryset = SwitchNetworkDevice.objects.all()
    serializer_class = SwitchSerializer


class RouterViewSets(viewsets.ModelViewSet):
    queryset = RouterNetworkDevice.objects.all()
    serializer_class = RouterSerializer


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
