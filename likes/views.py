from django.shortcuts import render
from .models import Like
from .serializers import LikeSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class LikeListCreate(APIView):
  def get(self, request):
    likes = Like.objects.all()
    serialized_likes = LikeSerializer(likes, many=True)
    return Response(data=serialized_likes.data, status=status.HTTP_200_OK)

  def post(self, request):
    like_serialzer = LikeSerializer(data=request.data)
    if like_serialzer.is_valid():
      like_serialzer.save()
      return Response(data=like_serialzer.data, status=status.HTTP_201_CREATED)
    return Response(data=like_serialzer.errors, status=status.HTTP_400_BAD_REQUEST)