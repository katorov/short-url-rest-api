from rest_framework import serializers

from shortener import models


class ShortLinkRetrieveSerializer(serializers.ModelSerializer):
    """Serializer для просмотра коротких ссылок"""

    class Meta:
        model = models.ShortLink
        fields = ['url', 'short_url']


class ShortLinkCreateSerializer(serializers.ModelSerializer):
    """Serializer для создания коротких ссылок"""

    class Meta:
        model = models.ShortLink
        fields = ['url', 'short_url', 'secret_key']
        read_only_fields = ['short_url', 'secret_key']
