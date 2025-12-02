from django.conf import settings
from django.core.mail import send_mail
from .models import Contact


def get_contact_email():
    """Возвращает email из первой записи Contact или выбрасывает исключение."""
    contact = Contact.objects.first()
    if not contact or not contact.email:
        raise ValueError("No contact email configured")
    return contact.email


def send_feedback_email(name, phone, comment):
    """Формирует и отправляет письмо с отзывом."""
    recipient_email = get_contact_email()

    subject = f'Новая заявка от {name}'
    message = (
        f"Имя: {name}\n"
        f"Телефон: {phone}\n"
        f"Комментарий: {comment}"
    )

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_email],
        fail_silently=False
    )
