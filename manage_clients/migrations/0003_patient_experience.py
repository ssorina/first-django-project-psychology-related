# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_clients', '0002_auto_20141208_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='experience',
            field=models.TextField(default=2, blank=True),
            preserve_default=False,
        ),
    ]
