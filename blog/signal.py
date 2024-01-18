from .utils import extract_text_from_html
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Post


@receiver(pre_save, sender=Post)
def create_serializer(sender, instance, **kwargs):
    instance.extracted_body = extract_text_from_html(instance.body)