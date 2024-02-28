
from .routers import router
from django.urls import path, include

from .views.RouterRunConfigView import RouterRunConfig
from .views.SwitchRunConfigView import SwitchRunConfig

urlpatterns = [
    path('rt-run-conf/<int:pk>', RouterRunConfig.as_view(), name="rt-run-conf"),
    path('sw-run-conf/<int:pk>', SwitchRunConfig.as_view(), name="sw-run-conf"),
    path('api/v1/', include(router.urls))
]
