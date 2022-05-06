from rest_framework.views import APIView
from rest_framework.response import Response
import pdf2image
import base64


class ImageAPIView(APIView):

    def post(self, request):

        decode = base64.b64decode(request.data["file"].encode('ascii'))
        img = pdf2image.convert_from_bytes(decode)

        base64img = base64.b64encode(img[0].tobytes())
        data = {'base64img': base64img}

        return Response(data)

