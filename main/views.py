from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Blog
from .serializers import BlogSerializer, PaginatedBlogSerializer

class CustomPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'totalPosts': self.page.paginator.count,
            'totalPages': self.page.paginator.num_pages,
            'currentPage': self.page.number,
            'posts': data
        })

class BlogListCreateView(APIView):
    def get(self, request):
        paginator = CustomPagination()
        queryset = Blog.objects.all().order_by('-date_posted')
        page = paginator.paginate_queryset(queryset, request)
        serializer = BlogSerializer(page, many=True)
        paginated_serializer = PaginatedBlogSerializer({
            'totalPosts': paginator.page.paginator.count,
            'totalPages': paginator.page.paginator.num_pages,
            'currentPage': paginator.page.number,
            'posts': serializer.data
        })
        return Response(paginated_serializer.data)


# @csrf_exempt
# def upload_image(request):
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