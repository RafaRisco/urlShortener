# Generated by Django 4.2.11 on 2024-03-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortsUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('short_url', models.CharField(max_length=200)),
                ('counter', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]