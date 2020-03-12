from django.urls import path,include
# from .views import
from music import views
from music import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'songs', views.SongsViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('songs/', SongsView.as_view(), name="songs-all"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]