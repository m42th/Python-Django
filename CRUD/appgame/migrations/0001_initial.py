# Generated by Django 4.0.4 on 2022-04-26 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('producer', models.CharField(max_length=255)),
                ('release', models.IntegerField()),
                ('platform', models.CharField(max_length=50)),
            ],
        ),
    ]
