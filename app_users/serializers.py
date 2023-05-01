from rest_framework import serializers
from django.contrib.auth import authenticate
from app_organizations.serializers import OrganizationSerializer
from app_organizations.models import Organizations

from .models import CustomUser
from .services import resize_image


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя.
    """

    organizations = OrganizationSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'telephone_number', 'avatar', 'organizations', )

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.telephone_number = validated_data.get('telephone_number', instance.telephone_number)
        avatar = validated_data.get('avatar')
        if avatar:
            instance.avatar = resize_image(avatar)
        instance.save()

        return instance


class UserRegisterSerializer(serializers.ModelSerializer):

    """
    Регистрация пользователя.
    """
    password = serializers.CharField(max_length=128, label='Введите пароль', write_only=True)
    password2 = serializers.CharField(max_length=128, label='Повторите пароль', write_only=True)

    class Meta:

        model = CustomUser
        fields = ('email', 'password', 'password2', 'first_name', 'last_name', 'telephone_number')

    def save(self, *args, **kwargs):

        user = CustomUser(
            email=self.validated_data['email'],
            first_name=self.validated_data.get('first_name', ''),
            last_name=self.validated_data.get('last_name', ''),
            telephone_number=self.validated_data.get('telephone_number', '')
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({password: 'Пароль не совпадает'})

        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """
    Авторизации пользователя.
    """

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):

        email = data.get('email')
        password = data.get('password')

        if email is None:
            raise serializers.ValidationError('Для входа в систему требуется адрес электронной почты.')

        if password is None:
            raise serializers.ValidationError('Для входа в систему требуется пароль.')

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('Пользователь с таким email и паролем не найден.')

        data['user'] = user

        return data


class OrganizationsUserSerializers(serializers.ModelSerializer):

    users = UserSerializer

    class Meta:

        model = Organizations
        fields = ('name', 'description', 'users', )


# def to_representation(self, instance):
#     ret = super().to_representation(instance)
#     ret.pop('organizations', None)
#     return ret
