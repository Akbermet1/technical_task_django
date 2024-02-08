from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryListCreateView(APIView):
    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        return Response("post method!")
