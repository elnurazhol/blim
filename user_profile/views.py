from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from djoser.views import UserViewSet as DjoserUserViewSet
from user_profile.models import Profile
from user_profile.serializers import ProfileSerializer

class ProfileCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        user = self.request.user  # Получаем текущего пользователя
        profile = serializer.save(user=user)
        return profile