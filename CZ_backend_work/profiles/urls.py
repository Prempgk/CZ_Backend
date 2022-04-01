
"""
from django.urls import path
from . import views

urlpatterns = [
    path('staffprofile',views.staffprofileApi),
    path('staffprofile/([0-1000]+)',views.staffprofileApi),
]
"""

from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()

router.register('staffprofile',staffprofileviewset)
router.register('staffqualification',staffqualviewset)
router.register('staffexperience',staffexpviewset)
urlpatterns = [
    path('v1/',include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)