from rest_framework.views import APIView
from rest_framework.response import Response
import pdf2image
import base64
from io import BytesIO


class ImageAPIView(APIView):

    def post(self, request):

        decode = base64.b64decode(request.data["file"])
        img = pdf2image.convert_from_bytes(decode)
        
        buf = BytesIO()
        img[0].save(buf, format="JPEG")
        
        base64img = base64.b64encode(buf.getvalue())
        data = {'base64img': base64img}

        return Response(data)

