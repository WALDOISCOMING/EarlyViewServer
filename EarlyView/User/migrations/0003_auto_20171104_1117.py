# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_remove_normaluser_user_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='normaluser',
            options={},
        ),
        migrations.AlterModelManagers(
            name='normaluser',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='normaluser',
            old_name='user_birthday',
            new_name='birthday',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='username',
        ),
    ]
