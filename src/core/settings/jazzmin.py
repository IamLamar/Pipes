JAZZMIN_SETTINGS = {
    # Общие настройки
    "site_title": "Трубный формат",
    "site_header": "Управление сайтом",
    "site_brand": "Трубный формат",
    "welcome_sign": "Добро пожаловать!",
    "site_logo_classes": "img-circle",  # Класс для логотипа (например, круглый)
    "user_avatar": None,  # Укажи поле аватарки пользователя, если есть

    # **Настройки бокового меню**
    "show_ui_builder": True,  # Отключаем UI Builder
    "navigation_expanded": True,  # Меню развернуто по умолчанию
    "order_with_respect_to": ["your_app", "auth", ],  # Порядок отображения приложений

    # **Настройки цветов и интерфейса**
    "theme": "flatly",  # Светлая тема для интерфейса

    # **Кастомизация форм и таблиц**
    "related_modal_active": True,  # Открывать связанные модели в модальных окнах
    "changeform_format": "horizontal_tabs",  # Формат вкладок для полей формы
    "language_chooser": False,  # Включаем переключатель языков

    # **Настройки для улучшения интерфейса**
    "search_fields": ['name', 'description'],  # Улучшение поиска
    "list_filter": ['category', 'status'],  # Фильтры в списке объектов
    "list_per_page": 25,  # Количество элементов на одной странице

    # **Стилизация и улучшение формы**
    "form_style": "horizontal",  # Горизонтальные формы для улучшенного восприятия
    "form_overrides": {
        "your_app.ModelName": {
            "field_1": {"widget": "django.forms.Textarea"},
            "field_2": {"widget": "django.forms.Select"},
        },
    },
}



JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-lightblue",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}
