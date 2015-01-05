# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('illness', models.CharField(max_length=1, choices=[(b'AF_D', b'affective disorders'), (b'ANX_D', b'anxiety disorders'), (b'DD', b'developmental disorders'), (b'PD', b'personality disorders'), (b'MH', b'adjustment and minor problems')])),
                ('age', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Psychologist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('session_price', models.IntegerField()),
                ('experience_level', models.CharField(max_length=1, choices=[(b'N', b'novice'), (b'I', b'intermmediate'), (b'E', b'experienced')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PsychOpinion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patient',
            name='psychologist',
            field=models.ForeignKey(to='manage_clients.Psychologist'),
            preserve_default=True,
        ),
    ]
