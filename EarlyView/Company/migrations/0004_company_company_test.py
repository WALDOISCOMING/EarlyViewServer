# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0003_auto_20170827_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_test',
            field=models.ForeignKey(null=True, to='Company.img'),
        ),
    ]
