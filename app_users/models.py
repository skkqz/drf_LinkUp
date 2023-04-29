from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
from app_organizations.models import Organizations


class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя
    """

    username = None
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message='Введите пожалуйста свой номер телефона в формате: +79999999999')
    telephone_number = models.CharField(validators=[phone_regex], null=True, blank=True, max_length=12, verbose_name=
                                        'Номер телефона')
    avatar = models.ImageField(upload_to='media/avatars', blank=True, verbose_name='Аватар')
    organizations = models.ManyToManyField(Organizations, blank=True, related_name='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
