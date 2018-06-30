from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('users', views.ListUser.as_view()),
    path('medical-conditions', views.ListMedicalCondition.as_view()),
    path('groups', views.ListGroup.as_view()),

    #path('users/<slug:pk>/', views.DetailUser.as_view()),
    # note : pk_abbrev is a slug
    re_path(r'users/mobile_num/(?P<mobileNum>(\d{3})-(\d{3})-(\d{4}))/abbrev/(?P<abbrev>[\w]+)$', views.DetailUser.as_view()),
    #re_path(r'users/mobile_num/(?P<mobileNum>(\d{3})-(\d{3})-(\d{4}))$', views.DetailUser.as_view()),
    #re_path(r'users/mobile_num/(?P<pk_mobile_num>[0-9]+)$', views.DetailUser.as_view()),
    #path('groups/<int:pk>/', views.DetailGroup.as_view()),
    #path('^groups/(?P<mobile_num>.+)/$', views.GroupMembersList.as_view()),
    path('group-members', views.GroupMembersList.as_view()),
    path('medical-conditions/<int:pk>/', views.DetailMedicalCondition.as_view()),

    path('rest-auth/', include('rest_auth.urls')),
]
