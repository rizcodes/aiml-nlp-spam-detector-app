import json
from json.decoder import JSONDecodeError

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


# Create your views here.
class CheckSpamView(APIView):
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        try:
            data = json.loads(request.body)
            messages = data.get('input', [])
            if not len(messages):
                response = {'error': 'No input messages received provided.'}
            else:
                response = {
                    'message': 'ham'
                }
        except JSONDecodeError:
            response = {'error': 'No payload.'}

        return Response(response, 400)
