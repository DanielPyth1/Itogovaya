from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import NetworkNode, Product
from .serializers import NetworkNodeSerializer, ProductSerializer
from .permissions import IsActiveUser
from rest_framework.response import Response
from rest_framework import status


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']

    def create(self, request, *args, **kwargs):
        if NetworkNode.objects.filter(name=request.data.get('name'), email=request.data.get('email')).exists():
            return Response(
                {"detail": "Объект с таким именем и email уже существует."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]
