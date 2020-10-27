from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from virus.serializer import VirusSerializer

# Create your views here.
class VirusView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = VirusSerializer(data=request.data)
        if serializer.is_valid():
            virus = serializer.save()
            return Response(f"Virus Created: Name:{virus.virusName}", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)