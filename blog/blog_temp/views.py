from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    
class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['put'])
    def friends(self, request):
        user = User.objects.get(pk = request.data['id'])
        friend = User.objects.get(pk = request.data['friend_id'] )
        user.add_friend(friend)
        friend.add_friend(user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    @action(detail=False, methods=['put'])
    def like(self, request):
        try:
            post = Post.objects.get(pk = request.data['id'])
            post.like += 1
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({'message': 'Ошибка'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['put'])
    def dislike(self, request):
        try:
            post = Post.objects.get(pk = request.data['id'])
            post.dislike += 1
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({'message': 'Ошибка'}, status=status.HTTP_404_NOT_FOUND)
        
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Create your views here.
