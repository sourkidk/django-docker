# basic URL Configurations
from django.urls import include, path
from rest_framework import routers
from apis import views

# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
# router.register(r'key', KeyViewSet)
router.register(r'key', views.KeyViewSet)
# router.register(r'key', views.)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('create/', views.CreateKeyViewSet.as_view(), name='create_key'),
    # path('update/<pk>', views.UpdateKeyViewSet.as_view(), name='update_key'),
    path('increment/<pk>', views.IncrementKeyViewSet.as_view(), name='update_key'),
]