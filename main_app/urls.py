from django.urls import path
from . import views

urlpatterns = [
    path('',                         views.home,                  name='home'),
    path('about/',                   views.about,                 name='about'),
    path('clows/',                   views.ClowList.as_view(),    name='clows_index'),
    path('clows/<int:pk>',           views.ClowDetail.as_view(),  name='clows_detail'),
    path('clows/create',             views.ClowCreate.as_view(),  name='clows_create'),
    path('clows/<int:pk>/update/',   views.ClowUpdate.as_view(),  name='clows_update'),
    path('clows/<int:pk>/delete/',   views.ClowDelete.as_view(),  name='clows_delete'),
]
