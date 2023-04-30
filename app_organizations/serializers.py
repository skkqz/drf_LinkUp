from rest_framework import serializers
from .models import Organizations


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Сериализатор организации.
    """

    class Meta:
        model = Organizations
        fields = ('id', 'name', 'description', )

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
