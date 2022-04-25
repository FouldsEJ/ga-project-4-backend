from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PopulatedPostSerializer, PostSerializer
from rest_framework import status


# Create your views here.



class PostListCreate(APIView):
  def get(self, request):
    posts = Post.objects.order_by('-created_datetime')
    serialized_posts = PopulatedPostSerializer(posts, many=True)
    return Response(data=serialized_posts.data, status=status.HTTP_200_OK)

  def post(self, request):
    post_serialzer = PostSerializer(data=request.data)
    if post_serialzer.is_valid():
      post_serialzer.save()
      return Response(data=post_serialzer.data, status=status.HTTP_201_CREATED)
    return Response(data=post_serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer