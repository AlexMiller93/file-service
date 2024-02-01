from django.urls import path
from api.views import FileUploadView, FileListView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='upload'),
    path('files/', FileListView.as_view(), name='files'),
]
