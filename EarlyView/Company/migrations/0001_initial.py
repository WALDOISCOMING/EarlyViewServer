# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0002_auto_20170827_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('company_content', models.CharField(max_length=30)),
                ('company_industry', models.CharField(max_length=30)),
                ('category', models.ForeignKey(to='Category.Category', on_delete=django.db.models.deletion.SET_NULL, null=True)),
            ],
        ),
    ]
