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

#class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    #queryset = models.User.objects.all()
    #serializer_class = serializers.UserSerializer

class ListGroup(generics.ListCreateAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = "mobileNum"
    lookup_url_kwarg = "mobileNum"
    #lookup_url_kwarg = "pk_mobile_num"

    def get_object(self):
        #mobile_num = self.kwargs['pk_mobile_num']
        mobile_num = self.kwargs.get(self.lookup_url_kwarg)
        abbrev = self.kwargs.get("abbrev")
        print ("shiva_1:abbrev=" + abbrev)
        print ("shiva:mobile_num=" + mobile_num)
        #return models.User.objects.filter(mobileNum=mobile_num)

        #abbrev = self.kwargs['pk_abbrev']
        #return models.User.objects.filter(mobileNum=mobile_num, abbrev=abbrev)

        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        #filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg], "abbrev":abbrev}
        obj = get_object_or_404(queryset,
                                **filter_kwargs)  # <-- can see that filtering is performed on the base of 'lookup_field'

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj  # will return the single retrieved object

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

