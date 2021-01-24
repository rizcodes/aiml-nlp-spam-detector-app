import json
from json.decoder import JSONDecodeError

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from app_spam_detector.core import MessageDetection

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
                status_code = 400
            else:
                output = []
                for msg in messages:
                    message = MessageDetection(msg)
                    category = message.classify()
                    output.append(category)
                response = {'input': messages, 'output': output}
                status_code = 200
        except JSONDecodeError:
            response = {'error': 'No payload.'}
            status_code = 400

        return Response(response, status_code)
