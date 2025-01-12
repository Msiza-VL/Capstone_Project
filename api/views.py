from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ActivitySerializer
from rest_framework import permissions
from activities.models import Activity
from .permissions import IsAuthenticatedOrCreate
from rest_framework import serializers

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthenticatedOrCreate]


    def get_queryset(self):

        return Activity.objects.filter(organiser=self.request.user)


    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(organiser=self.request.user)
        else:
            raise serializers.ValidationError("User is not authenticated")
