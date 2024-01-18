# Generated by Django 4.1.3 on 2022-11-20 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('termwork', '0002_loginform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('summary', models.TextField()),
            ],
        ),
    ]
