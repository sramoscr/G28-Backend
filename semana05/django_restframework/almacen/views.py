from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CategoryModel, ProductModel
from .serializers import CategorySerializer, ProductSerializer

class CategoryView(APIView):
    """
    API view para listar las categorias
    """
    def get(self, request):
        categories = CategoryModel.objects.all()

        # response = []
        # for category in categories:
        #     print(category.name)
        #     response.append({
        #         'id': category.id,
        #         'name': category.name
        #     })

        # return Response(response, status=status.HTTP_200_OK)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all() # queryset indica solo de donde se va a sacar la información "ProducModel"
    serializer_class = ProductSerializer #serializer hace la magia: validar y parsear

class ProductByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all() 
    serializer_class = ProductSerializer