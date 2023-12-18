# Generated by Django 5.0 on 2023-12-18 11:35

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AddField(
            model_name='book',
            name='bookFile',
            field=models.FileField(null=True, upload_to='books', verbose_name='Файл с книгой'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=100, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=100, verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=100, verbose_name='Издательство'),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='Unknown Title', max_length=100, verbose_name='Название книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='yearOfRel',
            field=models.IntegerField(default=2023, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)], verbose_name='Год выпуска'),
        ),
        migrations.AlterField(
            model_name='book',
            name='photoPreview',
            field=models.ImageField(null=True, upload_to='cover', verbose_name='Изображения'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('lastName', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('middle_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('dateOfBirth', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'unique_together': {('name', 'lastName', 'middle_name', 'dateOfBirth')},
            },
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.author', verbose_name='Автор'),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'author', 'yearOfRel', 'publisher')},
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
