from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.cache import cache


from .models import User
from .serializers import RegisterSerializer, UserSerializer
from .permissions import IsAdmin


# Register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.save()
        cache.delete("users_list")  # invalidate cache



# Login (JWT)
class LoginView(TokenObtainPairView):
    pass


# Protected profile
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# Admin-only endpoint
class AdminOnlyView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({
            "message": "Welcome Admin. You have access to this endpoint."
        })

#-----------------------------------------------------------------

# Cached Users List (Task 4)
class CachedUsersView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cache_key = "users_list"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        cache.set(cache_key, serializer.data, timeout=300)  # 5 minutes

        return Response(serializer.data)
