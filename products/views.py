from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(
    viewsets.GenericViewSet, 
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    """ ViewSet для получения списка продуктов и создания продукта """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductFormView(APIView):
    """ View для главной странице с продуктами и формой """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'products/product_form.html'

    @staticmethod
    def get(request):
        return Response()
