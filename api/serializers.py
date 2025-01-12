from rest_framework import serializers
from django.contrib.auth import get_user_model
from activities.models import Activity

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:

        model = Activity

        fields = '__all__'