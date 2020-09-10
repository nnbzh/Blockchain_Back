from rest_framework import serializers

from api.models import CurrencyRecord


class CurrencySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CurrencyRecord
        fields = '__all__'
