# Generated by Django 4.0.5 on 2023-05-11 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='articles/')),
                ('about', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True, null=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('about', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True, verbose_name='Контактный телефон')),
                ('organization', models.CharField(blank=True, max_length=50, null=True, verbose_name='Учреждение')),
                ('about', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Фото')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_org', models.BooleanField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.article')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.event')),
            ],
        ),
        migrations.CreateModel(
            name='Article_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.article')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
