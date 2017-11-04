# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0003_auto_20170827_2113'),
        ('User', '0003_auto_20171104_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='category',
            field=models.ManyToManyField(to='Category.Category'),
        ),
        migrations.AddField(
            model_name='normaluser',
            name='email',
            field=models.EmailField(max_length=254, default='a@a.com'),
        ),
        migrations.AddField(
            model_name='normaluser',
            name='username',
            field=models.CharField(max_length=30, default='a'),
        ),
    ]
