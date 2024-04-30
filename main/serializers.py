from django.core.files import images

from .models import Profile, Product, Comment

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['my_comment']


class Productserializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'category', 'summary', 'full_content', 'price', 'quantity', 'comment']

    def get_comment(self, obj):
        product_comment = obj.comment.first()

        return product_comment.my_comment if product_comment else None


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}  # Убедитесь, что пароль


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'name', 'author', 'title', 'date', 'my_image']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['password'] = make_password(user_data['password'])
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile


class Ovenserializer(serializers.ModelSerializer):
    oven = serializers.SerializerMethodField()

    class Meta:
        oven = Product
        fields = ['name', 'category', 'summary', 'full_content', 'price', 'quantity', 'comment']

    def get_oven(self, obj):
        product_oven = obj.oven.first()

        return product_oven.my_oven if product_oven else None
