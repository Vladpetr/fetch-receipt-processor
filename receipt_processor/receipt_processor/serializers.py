from rest_framework import serializers
from django.core.validators import RegexValidator

class ReceiptItemSerializer(serializers.Serializer):
    shortDescription=serializers.CharField(required=True, allow_blank=False, trim_whitespace=True, validators=[RegexValidator('^[\\w\\s\\-]+$')])
    price=serializers.CharField(required=True, allow_blank=False, trim_whitespace=True, validators=[RegexValidator('^\\d+\\.\\d{2}$')])

class ReceiptSerializer(serializers.Serializer):
    # pattern "^\\S+$" listed in api.yml does not include some test cases (e.g., "M&M Corner Market")
    # thus, I excluded any validations by regex in "retailer" field
    retailer = serializers.CharField(required=True, allow_blank=False, trim_whitespace=True)
    purchaseDate = serializers.CharField(required=True, allow_blank=False, trim_whitespace=True, validators=[RegexValidator('^\d{4}-\d{2}-\d{2}$')])
    purchaseTime = serializers.CharField(required=True, allow_blank=False, trim_whitespace=True, validators=[RegexValidator('^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$')])
    items = ReceiptItemSerializer(many=True, required=True)
    total = serializers.CharField(required=True, allow_blank=False, trim_whitespace=True, validators=[RegexValidator('^\\d+\\.\\d{2}$')])







