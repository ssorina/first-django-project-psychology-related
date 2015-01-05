# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('manage_clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='next_session',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 8, 11, 59, 35, 373409, tzinfo=utc), verbose_name=b'session reservation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='illness',
            field=models.CharField(max_length=10, choices=[(b'AF_D', b'affective disorders'), (b'ANX_D', b'anxiety disorders'), (b'DD', b'developmental disorders'), (b'PD', b'personality disorders'), (b'MH', b'adjustment and minor problems')]),
            preserve_default=True,
        ),
    ]
