# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 12:38
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='paints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('product_type', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('finish_type', models.CharField(max_length=20)),
                ('coverage', models.CharField(max_length=30)),
                ('availability', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('best_for', models.CharField(max_length=10)),
                ('washability', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('eco_friendly', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('durability', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('image', models.CharField(max_length=1000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paint', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
