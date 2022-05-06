from django.urls import path
from upload.views import ImageAPIView


urlpatterns = [
    path('<str:filename>', ImageAPIView.as_view())
]