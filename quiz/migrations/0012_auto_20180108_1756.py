# Generated by Django 2.0b1 on 2018-01-08 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20171206_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='topic',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='content',
            field=models.TextField(help_text='The instructional content of this quiz.', verbose_name='Quiz Content'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(help_text='The title of this quiz.', max_length=140, verbose_name='Quizc Title'),
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]