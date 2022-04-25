from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import Chat
from .serializers import ChatSerializer, PopulatedChatSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# class ChatListCreate(ListCreateAPIView):
#     # queryset = Chat.objects.all()
#     serializer_class = PopulatedChatSerializer

#     def get_queryset(self):
#       queryset = Chat.objects.all()
#       roomid = self.request.query_params.get('roomid')
#       if roomid:
#         queryset = queryset.filter(room_id=roomid)
#       return queryset

class ChatListCreate(APIView):
  def get(self, request):
    chats = Chat.objects.order_by('created_datetime')
    roomid = self.request.query_params.get('roomid')
    if roomid:
      chats = chats.filter(room_id=roomid)
    serialized_chats = PopulatedChatSerializer(chats, many=True)
    return Response(data=serialized_chats.data, status=status.HTTP_200_OK)

  def post(self, request):
    chat_serialzer = ChatSerializer(data=request.data)
    if chat_serialzer.is_valid():
      chat_serialzer.save()
      return Response(data=chat_serialzer.data, status=status.HTTP_201_CREATED)
    return Response(data=chat_serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDetail(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

