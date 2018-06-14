from rest_framework.serializers import ModelSerializer

from .models import Order


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial')
        self.user = initial.get('user')

    def create(self, validated_data):
        return Order.objects.create(user=self.user, **validated_data)
