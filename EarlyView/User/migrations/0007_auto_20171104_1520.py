# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_normaluser_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normaluser',
            name='category',
        ),
        migrations.AddField(
            model_name='normaluser',
            name='category',
            field=models.CharField(default='a', max_length=30),
        ),
    ]
