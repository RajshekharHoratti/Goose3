# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from goose3 import Goose
# Create your views here.

class goose_url_data_fetch(APIView):
    def post(self, request):
        print("success")
        url = request.POST.get('url')
        g = Goose()
        article = g.extract(url=url)
        title = article.title
        clean_text = article.cleaned_text
        data = {
            "title":title,
            "body":clean_text
        }
        return JsonResponse(data, safe=False)
