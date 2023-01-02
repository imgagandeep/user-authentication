from user_auth.models import User
from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone_number",
            "gender",
            "type",
            "password",
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
