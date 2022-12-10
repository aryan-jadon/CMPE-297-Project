from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transformers import pipeline


# API View here
class ClassificationAPI(APIView):
    def get(self, request):
        return Response({"status": "success",
                         "data": "Success Request"},
                        status=status.HTTP_200_OK)

    def post(self, request):
        classifier = pipeline("zero-shot-classification",
                              model="facebook/bart-large-mnli")
        all_categories = [
            "Film & Animation",
            "Autos & Vehicles",
            "Music",
            "Pets & Animals",
            "Sports",
            "Short Movies",
            "Travel & Events",
            "Gaming",
            "Videoblogging",
            "People & Blogs",
            "Comedy",
            "Entertainment",
            "News & Politics",
            "How to & Style",
            "Education",
            "Science & Technology",
            "Nonprofits & Activism",
            "Movies",
            "Anime/Animation",
            "Action/Adventure",
            "Classics",
            "Comedy",
            "Documentary",
            "Drama",
            "Family",
            "Foreign",
            "Horror",
            "Sci-Fi/Fantasy",
            "Thriller",
            "Shorts",
            "Shows",
            "Trailers"
        ]

        sequence_to_classify = "Summarized Sentence"
        response = classifier(sequence_to_classify, all_categories, multi_label=True)
        result = {
            response['labels'][0]: response['scores'][0],
            response['labels'][1]: response['scores'][1],
            response['labels'][2]: response['scores'][2],
        }
        return Response({"status": "success",
                         "results": result},
                        status=status.HTTP_200_OK)
