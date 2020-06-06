# Generated by Django 3.0.5 on 2020-05-02 13:44

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pagesite', '0035_auto_20200430_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMasalah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'หมวดหมู่ masalah',
                'verbose_name_plural': 'ประเภท masalah',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Masalah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1000, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('answer', ckeditor.fields.RichTextField(blank=True)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('view', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagesite.CategoryMasalah')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes_masalah', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'masalah',
                'verbose_name_plural': 'เนื้อหา masalah',
                'ordering': ('question',),
            },
        ),
        migrations.CreateModel(
            name='CommentMasalah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('masalah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagesite.Masalah')),
                ('reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='pagesite.CommentMasalah')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]