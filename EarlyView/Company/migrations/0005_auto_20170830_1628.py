# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0004_company_company_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('companyImage_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RenameField(
            model_name='company',
            old_name='category',
            new_name='company_category',
        ),
        migrations.RemoveField(
            model_name='company',
            name='company_test',
        ),
        migrations.DeleteModel(
            name='img',
        ),
        migrations.AddField(
            model_name='companyimage',
            name='companyImage_company',
            field=models.ForeignKey(to='Company.Company', null=True),
        ),
    ]
