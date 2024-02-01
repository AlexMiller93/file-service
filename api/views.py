from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import File
from api.serializers import FileSerializer


class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.data, status=status.HTTP_400)
        

class FileListView(APIView):
    def get(self, request, *args, **kwargs):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)