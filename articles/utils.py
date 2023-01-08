import random
from django.utils.text import slugify


def instance_articles_title(instance, new_slug=None, save=False):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        random_int = random.randint(30, 5000)
        slug = f"{slug}-{random_int}"
        return instance_articles_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance
