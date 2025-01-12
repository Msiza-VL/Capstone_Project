from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ActivityViewSet

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('activities', ActivityViewSet)
urlpatterns = []

urlpatterns += router.urls