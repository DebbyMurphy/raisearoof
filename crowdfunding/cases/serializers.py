from rest_framework import serializers
from .models import Case, Pledge



class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.CharField()
    case_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class CaseSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()   
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    pledges = PledgeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Case.objects.create(**validated_data)


class CaseDetailSerializer(CaseSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
