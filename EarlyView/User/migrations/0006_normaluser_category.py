# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0003_auto_20170827_2113'),
        ('User', '0005_remove_normaluser_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='category',
            field=models.ManyToManyField(to='Category.Category'),
        ),
    ]
