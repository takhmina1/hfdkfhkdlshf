from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'new_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        new_password = validated_data.pop('new_password', None)
        user = User.objects.create_user(**validated_data)
        if new_password:
            user.set_password(new_password)
        user.save()
        return user

    def update(self, instance, validated_data):
        new_password = validated_data.pop('new_password', None)
        instance = super().update(instance, validated_data)
        if new_password:
            instance.set_password(new_password)
            instance.save()
        return instance



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("Учетная запись не активирована.")
                data['user'] = user
            else:
                raise serializers.ValidationError("Неверные учетные данные.")
        else:
            raise serializers.ValidationError("Необходимо указать email и пароль.")
        return data
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordVerifySerializer(serializers.Serializer):
    reset_code = serializers.CharField()

class LogoutSerializer(serializers.Serializer):
    pass


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
class ActivationCodeSerializer(serializers.Serializer):
    activation_code = serializers.CharField(max_length=6)

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=True,
        min_length=8,
        error_messages={"min_length": "Не менее 8 символов.", "required": "Это поле обязательно."}
    )
    confirm_password = serializers.CharField(
        required=True,
        min_length=8,
        error_messages={"min_length": "Не менее 8 символов.", "required": "Это поле обязательно."}
    )
