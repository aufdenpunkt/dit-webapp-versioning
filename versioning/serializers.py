# 3rd party
from rest_framework import serializers

# Application
from versioning.models import WebAppVersion


class CurrentWebAppVersionSerializer(serializers.Serializer):
    version_number = serializers.SerializerMethodField()

    def get_version_number(self, obj):
        try:
            return WebAppVersion.objects.get(in_stores=True).version_number
        except WebAppVersion.DoesNotExist:
            return None


class WebAppVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebAppVersion
        fields = [
            "version_number",
            "in_stores",
        ]
