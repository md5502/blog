from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models import UserAccount
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):

    STATUS_CHOICES = [
        ('Y', _('Yes')),
        ('N', _('No')),

    ]
    title = models.CharField(verbose_name=_("title"), max_length=255)
    slug = models.SlugField(null=True, unique=True, allow_unicode=True)
    status = models.CharField(verbose_name=_("displayed"), max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][0])

    created_at = models.DateTimeField(
        verbose_name=_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"), auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Post(models.Model):

    STATUS_CHOICES = [
        ('P', _('Published')),
        ('D', _('Draft')),
        ('R', _('reject'))
    ]
    title = models.CharField(verbose_name=_("title"), max_length=255)
    slug = models.SlugField(null=True, unique=True, allow_unicode=True)
    lead = models.CharField(verbose_name=_(
        "lead"), max_length=1024, blank=True, null=True)
    body = models.TextField(verbose_name=_("context"))
    thumbnail = models.ImageField(verbose_name=_(
        "thumbnail"), upload_to='posts', blank=True, null=True)
    author = models.ForeignKey(UserAccount, verbose_name=_(
        "author"), on_delete=models.CASCADE)
    status = models.CharField(
        _("status"), max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][0])
    publish_time = models.DateTimeField(
        verbose_name=_("published at"), default=timezone.now)

    created_at = models.DateTimeField(
        verbose_name=_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"), auto_now=True)

    category = models.ManyToManyField(
        Category, verbose_name=_("Categorys"), related_name='Categorys')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title


class Comment(models.Model):

    STATUS_CHOICES = [
        ('Y', _('Yes')),
        ('N', _('No')),

    ]
    body = models.TextField(verbose_name=_("comment text"))
    post = models.ForeignKey(Post, verbose_name=_(
        "related post"), on_delete=models.CASCADE, related_name='comments')
    status = models.CharField(verbose_name=_("displayed"), max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][0])

    publish_time = models.DateTimeField(
        verbose_name=_("published at"), default=timezone.now)

    created_at = models.DateTimeField(
        verbose_name=_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"), auto_now=True)

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title
