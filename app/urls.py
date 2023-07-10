#DEFAULTS
from django.urls import path, include
#VIEWS
from .views import LoginView


app_name = 'app'

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
]