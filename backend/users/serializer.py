from .models import User
from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
#from .models import Profile

class AdminRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def validate(self, data):
        # Check if a superuser already exists
        if User.objects.filter(is_superuser=True).exists():
            raise serializers.ValidationError({
                "admin": "Admin already registered. Try logging in."
            })

        return data

    def create(self, validated_data):
        # Create the superuser
        user = User.objects.create_superuser(
            #username=validated_data['email'],  
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar']


class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']

    