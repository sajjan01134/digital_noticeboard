from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "role",
            "password",
            "is_active",
            "department",
            "staff_name",
            "staff_mob"
        )
        extra_kwargs = {"password": {"write_only": True}}
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            role=validated_data.get("role"),
            staff_name = validated_data["staff_name"],
            department= validated_data["department"],
            staff_mob = validated_data["staff_mob"],
        )
        user.set_password(validated_data["password"])
        user.is_active = True
        user.save()
        return user
    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.role = validated_data.get("role", instance.role)
# Handle organization update if needed
        instance.save()
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
            instance.save()
        return instance