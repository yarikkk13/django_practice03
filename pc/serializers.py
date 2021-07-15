from django.core.validators import RegexValidator
from rest_framework import serializers

from .models import PCModel


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCModel
        fields = '__all__'

    brand = serializers.CharField(validators=[
        RegexValidator('^[a-zA-Z]{2,20}$', 'only alpha min 2ch max 20ch')
    ])
    model = serializers.CharField(max_length=20)
    ram = serializers.IntegerField(min_value=1, max_value=64)
    cpu = serializers.IntegerField(min_value=1.1, max_value=5.3)
    display = serializers.IntegerField(min_value=9, max_value=17)