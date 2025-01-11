from rest_framework import viewsets, permissions

from .models import Activity

from .serializers import ActivitySerializer

class ActivityViewSet(viewsets.ModelViewSet):

    serializer_class = ActivitySerializer

    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):

        return Activity.objects.filter(user=self.request.user)


    def perform_create(self, serializer):

        serializer.save(user=self.request.user)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]