from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import filters
from rest_framework.views import APIView
from .models import Post
from rest_framework.permissions import IsAuthenticated

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        post_data = PostSerializer(posts, many=True).data
        return Response(post_data)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the author of the post
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response({"detail": "You do not have permission to edit this post."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response({"detail": "You do not have permission to delete this post."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the author of the comment
        post = Post.objects.get(pk=self.request.data['post'])
        serializer.save(author=self.request.user, post=post)

    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response({"detail": "You do not have permission to edit this comment."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response({"detail": "You do not have permission to delete this comment."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
