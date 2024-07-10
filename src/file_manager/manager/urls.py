from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileViewSet, FolderViewSet

router = DefaultRouter()
router.register(r'files', FileViewSet)
router.register(r'folders', FolderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]