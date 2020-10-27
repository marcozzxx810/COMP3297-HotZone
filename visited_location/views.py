from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from visited_location.serializer import VisitedLocationRecordSerializer

# Create your views here.
class VisitedLocationView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = VisitedLocationRecordSerializer(data=request.data)
        if serializer.is_valid():
            vlocR = serializer.save()
            return Response(f"Visited Record Created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)