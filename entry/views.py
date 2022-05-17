from rest_framework.views import APIView
from rest_framework.response import Response
from predict.models import Prediction


class EntryAPIView(APIView):

    def get(self, request):
        user = request.data['user']
        entries = Prediction.objects.filter(user__exact=user)
        
        result = [(el.category, el.date) for el in entries]            
        
        return Response(result)

