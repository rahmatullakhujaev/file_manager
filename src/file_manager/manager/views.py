from rest_framework import viewsets, permissions
from .models import File, Folder
from .serializers import FileSerializer, FolderSerializer
from rest_framework.decorators import action

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def share(self,request, pk=None):
        file = self.get_object()
        user = User.objects.get(user=request.data['username'])
        file.shared_with.add(user)
        return Response({'status': 'file_shared'})

    @action(detail=True, methods=['post'])
    def set_permission(self, request, pk=None):
        file = self.get_object()
        user = User.objects.get(user=request.data['username'])
        if request.data['permission'] == 'edit':
            file.can_edit.add(user)
        return Response({'status': 'file_shared'})


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
