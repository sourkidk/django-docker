# basic URL Configurations
from django.urls import include, path
from rest_framework import routers
from apis import views

# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used

router.register(r'key', views.KeyViewSet)
router.register(r'dog', views.DogViewSet)

# Couldn't get the router to work as expected, so took it out for now.
# router.register(r'increment', views.IncrementKeyViewSet)



# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('increment/<pk>', views.IncrementKeyViewSet.as_view(), name='update_key'),
]