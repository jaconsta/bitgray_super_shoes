# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('total_in_shelf', models.PositiveIntegerField()),
                ('total_in_vault', models.PositiveIntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('store', models.ForeignKey(to='stores.Store')),
            ],
        ),
    ]
