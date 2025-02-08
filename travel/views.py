from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class TravelPackageViewSet(viewsets.ModelViewSet):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer


class ChatbotView(APIView):
    def post(self, request):
        user_message = request.data.get("message", "").lower()

        # Simple keyword-based responses
        if "cheapest" in user_message:
            response = "We have several budget-friendly packages! Would you like to explore?"
        elif "best" in user_message:
            response = "Our best packages include trips to Bali, Paris, and Japan. Which one interests you?"
        else:
            response = "I'm here to help! Can you tell me more about the kind of trip you're looking for?"

        return Response({"response": response}, status=status.HTTP_200_OK)