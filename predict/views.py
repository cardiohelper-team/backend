from rest_framework.response import Response
from rest_framework.views import APIView
from predict.converter import main
from .models import Prediction


class PredictAPIView(APIView):
    def post(self, request):
        try:
            res = main(request.data["image"])

            Prediction.objects.create(
                file=request.data["image"],
                category=res,
                user='user'
            )

            return Response({
                'prediction': res
            })
        except Exception as e:
            return Response(f'error: {e}')
