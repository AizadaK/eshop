from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, \
    ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import *
from .models import Good

class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

class OrderCreate(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderList(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderRetrieve(RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderUpdate(UpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()    


