# Generated by Django 2.0.5 on 2018-06-29 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_user_followers_count'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='who_sold_it',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.User'),
        ),
    ]
