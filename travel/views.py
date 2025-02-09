from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re


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