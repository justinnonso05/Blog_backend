from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Blog, Comment
from django.db.models import Q
from rest_framework import status, generics
from .serializers import BlogSerializer, PaginatedBlogSerializer, CommentSerializer

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
        
# class CommentListView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


class CommentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'  # Allow the client to set the limit
    max_page_size = 100  # Maximum number of comments per page



class CommentListView(APIView):
    def get(self, request):
        # Get the blog_id from the query params
        blog_id = request.query_params.get('blog_id')
        if not blog_id:
            return Response({'error': 'blog_id parameter is required'}, status=400)

        # Try to get the corresponding blog
        blog = get_object_or_404(Blog, id=blog_id)

        # Get all comments for the blog post
        comments = Comment.objects.filter(post=blog).order_by('-date_posted')

        # Get the total number of comments
        total_comments = comments.count()

        # Set up pagination
        paginator = CommentPagination()
        paginated_comments = paginator.paginate_queryset(comments, request)

        # Serialize the comments
        serializer = CommentSerializer(paginated_comments, many=True)

        # Format the response data like the image format
        formatted_comments = [
            {
                "name": comment["name"],  # Assuming your CommentSerializer has author_name
                "comment": comment["content"],  # Assuming CommentSerializer has content field
                "date_posted": comment["date_posted"] # Format the date
            }
            for comment in serializer.data
        ]

        # Return the response without pagination metadata like 'count', 'next', etc.
        return Response({
            'totalComments': total_comments,
            'comments': formatted_comments
        })
    
    def post(self, request):
        blog_id = request.query_params.get('blog_id')
        # Retrieve blog post using blog_id from URL
        blog = get_object_or_404(Blog, id=blog_id)

        # Extract name and content from the form data
        name = request.data.get('name')
        content = request.data.get('content')

        # Validate that name and content are provided
        if not all([name, content]):
            return Response({'error': 'name and content are required fields'}, status=400)

        # Create a new comment for the specified blog
        comment = Comment(post=blog, name=name, content=content)
        comment.save()

        # Serialize the newly created comment
        serializer = CommentSerializer(comment)

        # Return the response with serialized data
        return Response(serializer.data, status=status.HTTP_201_CREATED)