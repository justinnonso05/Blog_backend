from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Blog
from django.db.models import Q
from rest_framework import status
from .serializers import BlogSerializer, PaginatedBlogSerializer

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'


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
        search_query = request.query_params.get('query', None)
        queryset = Blog.objects.all().order_by('-date_posted')
        if search_query:
            queryset = queryset.filter(Q(title__icontains = search_query.lower()) | Q(category__icontains = search_query.upper()))

        page = paginator.paginate_queryset(queryset, request)
        serializer = BlogSerializer(page, many=True)
        paginated_serializer = PaginatedBlogSerializer({
            'totalPosts': paginator.page.paginator.count,
            'totalPages': paginator.page.paginator.num_pages,
            'currentPage': paginator.page.number,
            'posts': serializer.data
        })
        return Response(paginated_serializer.data)


class BlogDetailView(APIView):
    def get(self, request):
        slug = request.query_params.get('slug')  # Get the slug from the query parameters
        if slug:
            try:
                blog = Blog.objects.get(slug=slug)
                serializer = BlogSerializer(blog)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Blog.DoesNotExist:
                return Response({'error': 'Blog post not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Slug parameter is required'}, status=status.HTTP_400_BAD_REQUEST)