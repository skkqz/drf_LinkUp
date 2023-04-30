from django.contrib.auth import logout, login
from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app_organizations.models import Organizations
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer, UserRegisterSerializer, OrganizationsUserSerializers
from .permissions import IsOwner


class UsersAPIView(viewsets.ModelViewSet):

    """
    Представление для пользователя.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserUpdateProfileAPIView(RetrieveUpdateAPIView):

    """
    Представление профиля пользователя.
    """

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):

        """
        Поле organizations необязательно для изменений.
        """

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserRegisterAPIView(CreateAPIView):

    """
    Представление для регистрации пользователя.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        serializer = UserRegisterSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = UserSerializer(user).data
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class UserLoginAPIView(APIView):

    """
    Авторизация пользователя.
    """

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(status=status.HTTP_200_OK)


class UserLogoutAPIView(APIView):

    """
    Logout пользователя.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class OrgUsersAPIView(ListAPIView):

    """
    Представление списка организаций и пользователей связанных с ней.
    """
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsUserSerializers
