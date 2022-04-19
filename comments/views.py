from curses import reset_prog_mode
from comments.serializers import CommentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Comment


# Create your views here.

class CommentListCreate(APIView):
  def get(self, request):
    comments = Comment.objects.all()
    serialized_comments = CommentSerializer(comments, many=True)
    return Response(data=serialized_comments.data, status=status.HTTP_200_OK)

  def post(self, request):
    comment_serialzer = CommentSerializer(data=request.data)
    if comment_serialzer.is_valid():
      comment_serialzer.save()
      return Response(data=comment_serialzer.data, status=status.HTTP_201_CREATED)
    return Response(data=comment_serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentRetrieveUpdateDelete(APIView):
  def get(self, request, pk):
    comment = self.get_comment(pk=pk)
    serialized_comment = CommentSerializer(comment)
    return Response(data=serialized_comment.data, status=status.HTTP_200_OK)


  def put(self, request, pk):
    comment_to_update = self.get_comment(pk=pk)
    updated_comment = CommentSerializer(comment_to_update, data=request.data)
    if updated_comment.is_valid():
      updated_comment.save()
      return Response(data=updated_comment.data, status=status.HTTP_201_CREATED)
    return Response(data=updated_comment.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    comment_to_delete = self.get_comment(pk=pk)
    comment_to_delete.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def get_comment(self, pk):
    try:
      return Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
      raise NotFound(detaul="can't find that comment")

