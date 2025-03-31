from rest_framework import serializers
from chocolate.models import Product

class ChocolateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'product', 'type', 'release_date', 
            'foundry', 'vendor', 'process_size', 
            'tdp', 'die_size', 'transistors', 'freq',
            'fp16_gflops', 'fp32_gflops', 'fp64_gflops'
        ]
