# Generated by Django 3.1 on 2020-09-03 19:50

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
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.BooleanField(null=True)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('cv', models.CharField(help_text='Write about your gaming history!', max_length=250)),
                ('gameids', models.CharField(help_text='Please write the name of your professional accounts (Steam, EpicGames, RiotGames etc. ', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(help_text='Be careful with saving your poll. You will not be able to edit it again', max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('choice_number', models.IntegerField(default=2, help_text='Maximum is 7')),
                ('category', models.CharField(default='comparison', help_text='All lowercase', max_length=50)),
                ('creator', models.CharField(help_text='If you leave this blank, your username will not be published, only admins can see it.', max_length=50)),
                ('vdq', models.ManyToManyField(blank=True, related_name='user_voted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='polls/images/')),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
    ]
