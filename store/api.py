from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import OrderSerializer


class OrderViewSet(ViewSet):
    # POST /orders/
    def create(self, request):
        serializer = OrderSerializer(data=request.data, initial={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
