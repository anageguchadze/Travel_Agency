from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('travel-packages', TravelPackageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]