from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from case_record.serializer import CaseRecordSerializer

# Create your views here.
class CaseRecordView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = CaseRecordSerializer(data=request.data)
        if serializer.is_valid():
            case = serializer.save()
            return Response(f"Case Created: ID:{case.id}, ", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)