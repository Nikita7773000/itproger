from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from .models import Profile, Product, Comment, Oven

from .serializers import ProfileSerializer, Productserializer, Commentserializer, Ovenserializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):  # Добавление доп. полей в токен
        token = super().get_token(user)
        token['custom_field'] = user.custom_field
        return token

    def validate(self, attrs):  # Валидация токена
        data = super().validate(attrs)
        return data


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {
                "user_id": user.id,
                "message": "User registered successfully."
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductAPIView1(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializer
    authentication_classes = []
    permission_classes = []


class UserRegistrationView1(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Commentserializer
    authentication_classes = []
    permission_classes = []


class UserRegistrationView2(generics.CreateAPIView):
    queryset = Oven.objects.all()
    serializer_class = Ovenserializer
    authentication_classes = []
    permission_classes = []

