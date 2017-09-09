# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0003_auto_20170827_2113'),
        ('Company', '0002_auto_20170827_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='category',
        ),
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ManyToManyField(to='Category.Category'),
        ),
    ]
