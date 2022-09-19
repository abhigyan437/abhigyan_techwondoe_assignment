from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.authtoken import views as view
from .router import router as route

router = routers.DefaultRouter()
router.register(r'company',views.CompanyViewSet)
router.register(r'team',views.TeamViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth',include('rest_framework.urls',namespace='rest_framework')),
    path('api/', include(route.urls)),
    path('api-token-auth/', view.obtain_auth_token, name='api-token-auth'),

]