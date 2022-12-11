from __future__ import unicode_literals
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transformers import pipeline
import requests
from summarizer import Summarizer, TransformerSummarizer


# API View here
class ZeroShortSummarizerAPI(APIView):
    def get(self, request):
        return Response({"status": "success",
                         "data": "Success Request"},
                        status=status.HTTP_200_OK)

    def post(self, request):
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

        url = "http://127.0.0.1:8001/"
        payload = {'youtube_url': 'https://www.youtube.com/watch?v=KwlBLxeKj2k&ab_channel=CBSNews'}
        files = []
        headers = {}
        request_response = requests.request("POST", url, headers=headers, data=payload, files=files)

        response = summarizer(json.loads(request_response.text)['video_text'],
                              do_sample=False)

        return Response({"status": "success",
                         "results": response},
                        status=status.HTTP_200_OK)


class BertSummarizerAPI(APIView):
    def get(self, request):
        return Response({"status": "success",
                         "data": "Success Request"},
                        status=status.HTTP_200_OK)

    def post(self, request):
        bert_model = Summarizer()

        url = "http://127.0.0.1:8001/"
        payload = {'youtube_url': 'https://www.youtube.com/watch?v=KwlBLxeKj2k&ab_channel=CBSNews'}
        files = []
        headers = {}
        request_response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(request_response.text)
        bert_summary = ''.join(bert_model(json.loads(request_response.text)['video_text']))

        return Response({"status": "success",
                         "results": bert_summary},
                        status=status.HTTP_200_OK)


class GPTSummarizerAPI(APIView):
    def get(self, request):
        return Response({"status": "success",
                         "data": "Success Request"},
                        status=status.HTTP_200_OK)

    def post(self, request):
        url = "http://127.0.0.1:8001/"
        payload = {'youtube_url': 'https://www.youtube.com/watch?v=KwlBLxeKj2k&ab_channel=CBSNews'}
        files = []
        headers = {}
        request_response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(request_response.text)

        GPT2_model = TransformerSummarizer(transformer_type="GPT2", transformer_model_key="gpt2-medium")
        GPT2_summary = ''.join(GPT2_model(json.loads(request_response.text)['video_text']))

        return Response({"status": "success",
                         "results": GPT2_summary},
                        status=status.HTTP_200_OK)


class XLNETSummarizerAPI(APIView):
    def get(self, request):
        return Response({"status": "success",
                         "data": "Success Request"},
                        status=status.HTTP_200_OK)

    def post(self, request):
        url = "http://127.0.0.1:8001/"
        payload = {'youtube_url': 'https://www.youtube.com/watch?v=KwlBLxeKj2k&ab_channel=CBSNews'}
        files = []
        headers = {}
        request_response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(request_response.text)

        model = TransformerSummarizer(transformer_type="XLNet", transformer_model_key="xlnet-base-cased")
        xlnet_summary = ''.join(model(json.loads(request_response.text)['video_text']))

        return Response({"status": "success",
                         "results": xlnet_summary},
                        status=status.HTTP_200_OK)
