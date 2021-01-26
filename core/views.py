from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .serializers import *
from .models import Good

class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

class OrderCreate(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


