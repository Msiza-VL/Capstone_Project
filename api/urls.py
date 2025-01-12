from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ActivityViewSet
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('activities', ActivityViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]

urlpatterns += router.urls