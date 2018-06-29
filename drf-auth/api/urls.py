from django.urls import include, path

from . import views

urlpatterns = [
    path('users', views.ListUser.as_view()),
    path('medical-conditions', views.ListMedicalCondition.as_view()),
    path('groups', views.ListGroup.as_view()),

    path('users/<int:pk>/', views.DetailUser.as_view()),
    path('groups/<int:pk>/', views.DetailGroup.as_view()),
    #path('^groups/(?P<mobile_num>.+)/$', views.GroupMembersList.as_view()),
    path('group-members', views.GroupMembersList.as_view()),
    path('medical-conditions/<int:pk>/', views.DetailMedicalCondition.as_view()),

    path('rest-auth/', include('rest_auth.urls')),
]
