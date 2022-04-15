from rest_framework import serializers
from createlist.models import To_Do_List

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = To_Do_List
        fields = ['titel', 'date_add', 'note']
