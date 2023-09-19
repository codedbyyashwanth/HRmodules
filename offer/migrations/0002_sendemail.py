# Generated by Django 4.2.1 on 2023-09-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
