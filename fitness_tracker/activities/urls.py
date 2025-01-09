from django.urls import path
from .views import ActivityListAPIView, ActivityDetailAPIView, ActivityMetricsAPIView

urlpatterns = [
    path('activities/', ActivityListAPIView.as_view()),
    path('activities/<int:pk>/', ActivityDetailAPIView.as_view()),
    path('activities/metrics/', ActivityMetricsAPIView.as_view()),
]