from django.urls import include, path
from rest_framework import routers
from . import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(ROUTER.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]