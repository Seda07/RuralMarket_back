from .models import CustomUser
from rest_framework import generics, permissions, views, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserDetailSerializer, UserUpdateSerializer
from rest_framework.exceptions import ValidationError


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        email = request.data.get('email')

        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError({"username": "Este nombre de usuario ya está en uso. Por favor, elige otro."})

        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError({"email": "Este correo electrónico ya está en uso. Por favor, elige otro."})

        if CustomUser.objects.filter(first_name=first_name).exists():
            raise ValidationError({"first_name": "Este nombre ya está en uso. Por favor, elige otro."})

        return super().create(request, *args, **kwargs)


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"message": "Token deleted"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"message": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(user_type='seller')
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.AllowAny]