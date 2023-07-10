#DEFAULTS
from django.urls import path, include
#VIEWS
from .views import PartnerView


urlpatterns = [
    path('partners/', PartnerView.as_view(), name='partner'),
]