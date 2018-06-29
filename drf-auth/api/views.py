from rest_framework import generics
#from django.views.generic import ListView
import pdb

from Users import models
from . import serializers
from django.shortcuts import get_object_or_404


class ListUser(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class ListMedicalCondition(generics.ListCreateAPIView):
    queryset = models.MedicalCondition.objects.all()
    serializer_class = serializers.MedicalConditionSerializer

class DetailMedicalCondition(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MedicalCondition.objects.all()
    serializer_class = serializers.MedicalConditionSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class ListGroup(generics.ListCreateAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer

class DetailGroup(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer

class GroupMembersList(generics.ListAPIView):
    serializer_class = serializers.GroupMembersSerializer
    def get_queryset(self):
        #qs = super().get_queryset()
        #return qs.filter(mobile_num__=self.kwargs.mobile_num)
        #pdb.set_trace()
        #mobile_num = self.kwargs['mobile_num']
        mobile_num = self.request.query_params.get('query', None)

        #data = models.User.objects.all()
        return models.User.objects.filter(mobileNum__icontains=mobile_num)

