from django.contrib import admin
from django.urls import path, include
from predict.views import PredictAPIView
from upload.views import ImageAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/predict', PredictAPIView.as_view()),
    path('api/v1/upload', ImageAPIView.as_view()),
]
