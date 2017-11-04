# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20171104_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normaluser',
            name='category',
        ),
    ]
