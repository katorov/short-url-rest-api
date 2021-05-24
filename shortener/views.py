from django.shortcuts import redirect, get_object_or_404

from shortener.models import ShortLink


def redirect_to_long_url(request, short_link_id):
    """Перенаправить пользователя по короткой ссылке"""
    short_link = get_object_or_404(ShortLink, pk=short_link_id)
    return redirect(short_link.url)
