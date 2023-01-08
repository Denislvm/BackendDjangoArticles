from django.db import models
from .utils import instance_articles_title
from django.db.models.signals import pre_save, post_save


class Articles(models.Model):
    title = models.TextField()
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    if instance.slug is None:
        instance_articles_title(instance, save=False)


pre_save.connect(article_pre_save, sender=Articles)


def article_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        instance_articles_title(instance, save=True)


post_save.connect(article_post_save, sender=Articles)



