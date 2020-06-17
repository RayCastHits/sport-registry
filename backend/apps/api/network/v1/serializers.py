from rest_framework import serializers
from apps.api.registry.models import Sportsman, Primary, Medical, SportResult


class PrimarySerializer(serializers.ModelSerializer):
    """
    Сериализатор первичных обследований
    """

    # sport_result = SportResultSerializer()

    class Meta:
        model = Primary
        fields = "__all__"


class MedicalSerializer(serializers.ModelSerializer):
    """
    Сериализатор УМО
    """

    # sport_result = SportResultSerializer()

    class Meta:
        model = Medical
        fields = "__all__"


class SportsmanSerializer(serializers.ModelSerializer):
    """
    Сериализатор спортсмена
    """

    primary = PrimarySerializer(many=True, read_only=True)
    medical = MedicalSerializer(many=True, read_only=True)

    class Meta:
        model = Sportsman
        fields = "__all__"


class RelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Primary):
            serializer = PrimarySerializer(value)
        elif isinstance(value, Medical):
            serializer = MedicalSerializer(value)
        else:
            raise Exception("Unexpected type of tagged object")
        return serializer.data


class SportResultSerializer(serializers.ModelSerializer):
    """
    Сериализатор спортивных результатов
    """

    content_object = RelatedField(read_only=True)

    class Meta:
        model = SportResult
        fields = "__all__"
