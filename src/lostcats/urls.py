from django.urls import path
from lostcats import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("robots.txt", views.Robots.as_view(), name="robots"),
    path("map/", views.Map.as_view(), name="map"),
    path("cats/", views.Gallery.as_view(), name="gallery"),
    path("cats/<pk>/<slug>/", views.CatDetail.as_view(), name="cat-detail"),
    path("locate/", views.CatLocate.as_view(), name="cat-locate"),
    path("create/", views.CatCreate.as_view(), name="cat-create"),
]
