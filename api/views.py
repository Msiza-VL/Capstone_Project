from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ActivitySerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    #permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):

        return Activity.objects.filter(user=self.request.user)


    def perform_create(self, serializer):

        serializer.save(user=self.request.user)
