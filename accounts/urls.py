from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # django-allauth가 제공하는 모든 인증 URL(login, logout, signup 등)을 포함합니다.
    # 이 설정으로 /accounts/login/, /accounts/google/login/ 등의 주소가 활성화됩니다.
    path('', include('allauth.urls')),
    
]