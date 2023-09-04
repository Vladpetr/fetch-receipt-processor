from rest_framework import serializers
from django.core.validators import RegexValidator

class ReceiptItemSerializer(serializers.Serializer):
    shortDescription=serializers.CharField(required=True, allow_blank=False, trim_whitespace=True, validators=[RegexValidator('^[\\w\\s\\-]+$')])
    price=serializers.CharField(required=True, allow_blank=False, trim_whitespace=True, validators=[RegexValidator('^\\d+\\.\\d{2}$')])

class ReceiptSerializer(serializers.Serializer):
    retailer = serializers.CharField(required=True, allow_blank=False, trim_whitespace=True, validators=[RegexValidator('^\\S+$')])
    purchaseDate = serializers.CharField(required=True, allow_blank=False, trim_whitespace=True, validators=[RegexValidator('^\d{4}-\d{2}-\d{2}$')])
    purchaseTime = serializers.CharField(required=True, allow_blank=False, trim_whitespace=True, validators=[RegexValidator('^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$')])
    items = ReceiptItemSerializer(many=True, required=True)
    total = serializers.CharField(required=True, allow_blank=False, trim_whitespace=True, validators=[RegexValidator('^\\d+\\.\\d{2}$')])







