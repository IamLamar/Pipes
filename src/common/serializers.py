from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from django.db import models


class AbsoluteImageUrlMixin:
    """
    Автоматически превращает все ImageField в абсолютный URL.
    Работает только если миксин используется с ModelSerializer.
    """

    @classmethod
    def _build_absolute_url(cls, obj, field_name, request):
        image = getattr(obj, field_name, None)
        if image and request:
            return request.build_absolute_uri(image.url)
        return None

    @classmethod
    def _add_serializer_method_fields(cls):
        # Если нет Meta или model — просто пропускаем
        meta = getattr(cls, "Meta", None)
        model = getattr(meta, "model", None)

        if not model:
            return

        # Перебираем поля модели
        for field in model._meta.get_fields():
            if hasattr(field, "upload_to"):  # Признак FileField/ImageField
                if isinstance(field, models.ImageField):
                    method_name = f"get_{field.name}"

                    if not hasattr(cls, method_name):
                        def _method(self, obj, field_name=field.name):
                            request = self.context.get("request")
                            return self._build_absolute_url(obj, field_name, request)

                        # Для документации в Swagger
                        decorated = extend_schema_field(serializers.CharField())(_method)
                        setattr(cls, method_name, decorated)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._add_serializer_method_fields()
