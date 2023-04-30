from django.urls import path
from .views import UsersAPIView, UserLogoutAPIView, UserLoginAPIView,\
    UserRegisterAPIView, UserUpdateProfileAPIView, OrgUsersAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user_logout'),
    path('reg/', UserRegisterAPIView.as_view(), name='user_registration'),
    path('', UsersAPIView.as_view({'get': 'list'}), name='users_list'),
    path('<int:pk>/', UsersAPIView.as_view({'get': 'retrieve'}), name='user_detail'),
    path('profile/', UserUpdateProfileAPIView.as_view(), name='user_profile'),
    path('organizations-users/', OrgUsersAPIView.as_view(), name='organizations_users')
]
