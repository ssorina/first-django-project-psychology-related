# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_clients', '0004_auto_20141218_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='experience',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
