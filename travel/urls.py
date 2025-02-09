from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('travel-packages', TravelPackageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify/<uidb64>/<token>/', EmailVerificationView.as_view(), name='verify-email'),
]