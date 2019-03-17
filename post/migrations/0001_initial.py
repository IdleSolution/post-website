# Generated by Django 2.0.5 on 2018-06-23 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('posted_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('profile_description', models.TextField()),
                ('created_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='who_wrote_it',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.User'),
        ),
    ]
