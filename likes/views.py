from django.shortcuts import render
from .models import Like
from .serializers import LikeSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


# Create your views here.


class LikeListCreate(APIView):
  def get(self, request):
    likes = Like.objects.all()
    postid = self.request.query_params.get('postid')
    if postid:
      likes = likes.filter(post_id=postid)
    serialized_likes = LikeSerializer(likes, many=True)
    return Response(data=serialized_likes.data, status=status.HTTP_200_OK)

  def post(self, request):
    like_serialzer = LikeSerializer(data=request.data)
    if like_serialzer.is_valid():
      like_serialzer.save()
      return Response(data=like_serialzer.data, status=status.HTTP_201_CREATED)
    return Response(data=like_serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeRetrieveUpdateDelete(APIView):
  def get(self, request, pk):
    like = self.get_like(pk=pk)
    serialized_like = LikeSerializer(like)
    return Response(data=serialized_like.data, status=status.HTTP_200_OK)


  def put(self, request, pk):
    like_to_update = self.get_like(pk=pk)
    updated_like = LikeSerializer(like_to_update, data=request.data)
    if updated_like.is_valid():
      updated_like.save()
      return Response(data=updated_like.data, status=status.HTTP_201_CREATED)
    return Response(data=updated_like.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    like_to_delete = self.get_like(pk=pk)
    like_to_delete.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def get_like(self, pk):
    try:
      return Like.objects.get(pk=pk)
    except Like.DoesNotExist:
      raise NotFound(detail="can't find that like")