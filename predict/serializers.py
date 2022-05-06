from rest_framework.serializers import ModelSerializer
from .models import Prediction


class PredictSerializer(ModelSerializer):
    class Meta:
        model = Prediction
        fields = ('file', 'category', 'owner')