from rest_framework import routers
from .viewsets import UserViewSets, RouterViewSets, SwitchViewSets

router = routers.DefaultRouter()
router.register(
    "users",
    UserViewSets,
    basename='users_viewsets'
)
router.register(
    "routers",
    RouterViewSets,
    basename='routers_viewsets'
)
router.register(
    "switches",
    SwitchViewSets,
    basename='switches_viewsets'
)
