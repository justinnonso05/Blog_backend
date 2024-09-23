from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from cloudinary.uploader import upload
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer



@csrf_exempt
def upload_image(request):
    ...
    # if request.method == 'POST' and request.FILES:
    #     file = request.FILES['file']
    #     result = upload(file, folder="Blog/content/")  # Upload directly to Cloudinary
    #     image_url = result.get('url')  # Get the Cloudinary URL

    #     return JsonResponse({
    #         'url': image_url,
    #         'name': file.name
    #     })
    # return JsonResponse({'error': 'Invalid request'}, status=400)