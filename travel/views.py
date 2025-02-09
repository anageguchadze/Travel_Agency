from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator as token_generator, default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class TravelPackageViewSet(viewsets.ModelViewSet):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer


class ChatbotView(APIView):
    def post(self, request):
        user_message = request.data.get("message", "").lower()
        
        if not user_message:
            return Response({"error": "No message provided!"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Enhanced pattern matching for better responses
        if re.search(r"\b(cheap|affordable|budget|low price)\b", user_message):
            response = "We have budget-friendly packages to places like Bali, Thailand, and Vietnam! Would you like to explore more?"
        
        elif re.search(r"\b(best|top|recommended)\b", user_message):
            response = "Our best packages include destinations like Bali, Paris, and Japan. Which one are you interested in?"
        
        elif re.search(r"\b(price|cost|expensive)\b", user_message):
            response = "We offer a range of prices! Do you have a specific budget in mind?"
        
        elif re.search(r"\b(duration|length)\b", user_message):
            response = "How many days are you planning for your trip? We have packages ranging from 3 days to 2 weeks."
        
        elif re.search(r"\b(destination|place|where)\b", user_message):
            response = "Our popular destinations include Bali, Paris, Japan, and New York. What kind of place are you looking for?"
        
        elif re.search(r"\b(hello|hi|hey|greetings)\b", user_message):
            response = "Hi there! How can I assist you with your travel plans today?"
        
        else:
            # Fallback response when no specific pattern is matched
            response = "I'm here to help! Could you tell me a bit more about the trip you're looking for?"

        return Response({"response": response}, status=status.HTTP_200_OK)
    

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Generate a verification token and send email
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(user.pk.encode())
            domain = get_current_site(request).domain
            verification_url = f'http://{domain}/verify/{uid}/{token}/'
            
            # Send email to user
            subject = "Verify your email address"
            message = f"Please click the following link to verify your email address: {verification_url}"
            send_mail(subject, message, 'from@example.com', [user.email])

            return Response({"message": "User registered successfully. Please check your email for verification."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EmailVerificationView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_user_model().objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.is_verified = True
                user.is_active = True  # Activate the user
                user.save()
                return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid verification link."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            if user.is_active and user.is_verified:
                # If user is authenticated, active, and verified, generate token
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Account is not activated or verified."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)