# library/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import forms
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # ... остальные поля

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_user_groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_permissions',
    )

class Cover(models.Model):
    def validate_image(value):
        size_limit = 2 * 1024 * 1024
        if value.size > size_limit:
            raise forms.ValidationError('Файл слишком большой. Размер файла не должен превышать 2MB')

    cover = models.ImageField(validators=[validate_image], upload_to='cover/books/title', verbose_name='Изображения',
                              blank=True, null=False)

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')


class Book(models.Model):
    # ... остальные поля

    def validate_image(value):
        size_limit = 2 * 1024 * 1024
        if value.size > size_limit:
            raise forms.ValidationError('Файл слишком большой. Размер файла не должен превышать 2MB')

    photoPreview = models.ImageField(validators=[validate_image], upload_to='cover', verbose_name='Изображения',
                                     blank=True, null=True)
