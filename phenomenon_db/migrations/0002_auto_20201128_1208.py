# Generated by Django 2.0.12 on 2020-11-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phenomenon_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seaphenomenon',
            name='source_link',
            field=models.URLField(blank=True, help_text='Ссылка', max_length=500, null=True, verbose_name='Источник'),
        ),
    ]
