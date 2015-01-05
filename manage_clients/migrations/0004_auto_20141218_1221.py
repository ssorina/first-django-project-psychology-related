# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_clients', '0003_patient_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='experience',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
