from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from chocolate.models import Product
from chocolate.serializers import ChocolateSerializer
from .renderers import CSVRenderer  # Импортируем CSV-рендерер

class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ChocolateSerializer
    renderer_classes = [JSONRenderer, CSVRenderer]  # Добавляем поддержку CSV