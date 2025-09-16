from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .ml.utils import predict_url


def home(request):
    return render(request, 'index.html')


class UrlChecker(APIView):
    def post(self, request):
        urls = request.data.get('url')
        if not urls:
            return Response( {"error": "URL is required"},status=400)
        results = {}
        for u in urls:
            results[u] = predict_url(u)

        return Response(results)

