# Generated by Django 2.0b1 on 2017-11-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20171126_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
