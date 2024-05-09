# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-30 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmnad', '0013_remove_grant_order_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='date_end',
            field=models.DateField(blank=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0446\u0430 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AddField(
            model_name='people',
            name='date_start',
            field=models.DateField(blank=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b'),
        ),
        migrations.AddField(
            model_name='people',
            name='status',
            field=models.BooleanField(choices=[(0, '\u041d\u0435\u0442'), (1, '\u0414\u0430')], default=1, verbose_name='\u0420\u0430\u0431\u043e\u0442\u0430\u0435\u0442'),
        ),
    ]
