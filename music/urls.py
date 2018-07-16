from django.urls import path
from django.conf.urls import url
from . import views

app_name ='music'
urlpatterns = [
    path('album/add/',views.AlbumCreate.as_view(),name='album-add'),

    #/music/
    path('', views.IndexView.as_view(), name='index'),
    #/music/71/
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]