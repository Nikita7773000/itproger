from django.urls import path, include

from .views import UserRegistrationView, ProductAPIView1, UserRegistrationView1, UserRegistrationView2

urlpatterns = [
    path('api/glava/', ProductAPIView1.as_view()),
    path('api/vika/', UserRegistrationView.as_view(), name='token_obtain2_pasir'),
    path('api/token12/', UserRegistrationView1.as_view(), name='token_obtain2_pasir'),
    path('api/grait14/', UserRegistrationView2.as_view(), name='token_obtain2_pasir'),
]
