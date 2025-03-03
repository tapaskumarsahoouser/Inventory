from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from UserServices.models import UploadedFile

def index(request):
    return render(request, 'index.html')

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        uploaded_files_urls = []

        for file_key in request.FILES:
            file_obj = request.FILES[file_key]
            uploaded_file = UploadedFile.objects.create(file=file_obj)
            file_url = uploaded_file.file.url  # Get the URL of the uploaded file
            uploaded_files_urls.append(file_url)

        return Response({'message': 'File uploaded successfully', 'urls': uploaded_files_urls}, status=200)
