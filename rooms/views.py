from django.shortcuts import render

from rooms.serializers import RoomSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Room
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class RoomListCreate(APIView):
  def get(self, request):
    rooms = Room.objects.order_by('-created_datetime')
    userid = self.request.query_params.get('userid')
    roomname_search = self.request.query_params.get('search')
    if userid:
        rooms = rooms.filter(users=userid)
        if roomname_search:
            rooms = rooms.filter(name__icontains=roomname_search)
    serialized_rooms = RoomSerializer(rooms, many=True)
    return Response(data=serialized_rooms.data, status=status.HTTP_200_OK)

  def post(self, request):

    # name = request.data.get('name')
    # try: 
    #   Room.objects.get(name=name)
    #   return Response({'message': 'A chat room with this name already exists'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    # except Room.DoesNotExist:
    #   pass

    room_serialzer = RoomSerializer(data=request.data)
    if room_serialzer.is_valid():
      room_serialzer.save()
      return Response(data=room_serialzer.data, status=status.HTTP_201_CREATED)
    return Response(data=room_serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer


