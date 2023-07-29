from django.urls import path
from user_profile.views import ProfileCreateAPIView

urlpatterns = [
    path('profiles/', ProfileCreateAPIView.as_view(), name='profile-create'),
]