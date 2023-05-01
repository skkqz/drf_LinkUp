from rest_framework import serializers
from .models import Organizations
from app_users.models import CustomUser


class UsersSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя для отображения в организациях
    """

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'telephone_number', 'avatar', )


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Сериализатор организации.
    """

    users = UsersSerializer(many=True)

    class Meta:
        model = Organizations
        fields = ('id', 'name', 'description', 'users', )

    def create(self, validated_data):
        return Organizations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firs_name = validated_data.get('name', instance.firs_name)
        instance.last_name = validated_data.get('description', instance.last_name)
        instance.save()
        return instance


class CreateOrganizationSerializer(serializers.ModelSerializer):

    """
    Сериализатор для создания новой организации
    """

    class Meta:

        model = Organizations
        fields = ('name', 'description', )
