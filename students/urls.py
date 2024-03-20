from django.urls import path, include
from rest_framework import routers
from students import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentView, 'students')

urlpatterns = [
  path('api/v1/', include(router.urls)),
]