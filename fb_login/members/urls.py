from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('<int:pk>/', UserRetrieveView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]