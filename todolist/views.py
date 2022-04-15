from django.shortcuts import render,redirect
from createlist.models import To_Do_List
from createlist.forms import To_Do_ListForm
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from createlist.serializers import ListSerializer
from rest_framework import generics, mixins, status


def home(request):

    return render(request, 'home.html')

class PostList(generics.ListAPIView):
    queryset = To_Do_List.objects.all()
    serializer_class = ListSerializer


class Create(generics.CreateAPIView):
    queryset = To_Do_List.objects.all()
    serializer_class = ListSerializer

class Update(generics.UpdateAPIView, mixins.DestroyModelMixin):
    serializer_class = ListSerializer

    def get_queryset(self):
        return To_Do_List.objects.filter(id = self.kwargs['pk'])

    def perform_create(self, serializer):
         if self.get_queryset().exists():
             serializer.save()
    def delete(self, requests, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never insert this id!')
