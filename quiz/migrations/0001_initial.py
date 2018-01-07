# Generated by Django 2.0b1 on 2017-11-21 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answered_correctly', models.BooleanField(editable=False)),
                ('is_correct', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'User Answer',
                'verbose_name_plural': 'User Answers',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_in_quiz', models.PositiveIntegerField(verbose_name='Order in Quiz')),
                ('content', models.CharField(help_text='Enter question', max_length=1000, verbose_name='Question')),
                ('question', models.CharField(help_text="A question that can be answered with either 'Yes' or 'No'.", max_length=200, verbose_name='Question')),
                ('correct_answer', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Correct Answer')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ('order_in_quiz',),
            },
        ),
        migrations.CreateModel(
            name='QuestionAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='The title of this lesson.', max_length=140, verbose_name='Lesson Title')),
                ('content', models.TextField(help_text='The instructional content of this lesson.', verbose_name='Quiz Content')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
                'ordering': ('-date_created', '-date_modified', '-topic'),
            },
        ),
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.AddField(
            model_name='quiz',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Topic'),
        ),
        migrations.AddField(
            model_name='questionattempt',
            name='attempt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.QuizAttempt'),
        ),
        migrations.AddField(
            model_name='questionattempt',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
        ),
        migrations.AddField(
            model_name='questionattempt',
            name='response',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Answer'),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.Quiz'),
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Topic'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question', 'user')},
        ),
    ]