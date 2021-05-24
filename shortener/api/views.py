from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shortener import models
from shortener.api import serializers
from shortener.api.mixins import MultiSerializerViewSetMixin


class ShortLinkViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    """REST api для сокращения ссылок"""
    queryset = models.ShortLink.objects.all()
    http_method_names = ('get', 'post', 'delete')
    serializer_class = serializers.ShortLinkRetrieveSerializer
    serializer_action_classes = {
        'create': serializers.ShortLinkCreateSerializer,
    }

    def destroy(self, request, *args, **kwargs):
        """Удалить короткую ссылку (при условии совпадения секретного ключа)"""
        instance = self.get_object()
        secret_key = request.parser_context['kwargs'].get('secret_key', None)

        if not secret_key:
            raise ValidationError('Отсутствует секретный ключ')
        if secret_key != instance.secret_key:
            raise ValidationError('Неверный секретный ключ')

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
