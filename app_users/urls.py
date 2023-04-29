from django.urls import path
from .views import UsersAPIView, UserLogoutAPIView, UserLoginAPIView, UserRegisterAPIView, UserUpdateProfileAPIView

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='user_login'),
    path('users/logout/', UserLogoutAPIView.as_view(), name='user_logout'),
    path('users/reg/', UserRegisterAPIView.as_view(), name='user_registration'),
    path('users/', UsersAPIView.as_view({'get': 'list'}), name='users_list'),
    path('users/<int:pk>/', UsersAPIView.as_view({'get': 'retrieve'}), name='user_detail'),
    path('users/profile/', UserUpdateProfileAPIView.as_view(), name='user_profile'),
]
