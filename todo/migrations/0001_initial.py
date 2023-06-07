# Generated by Django 4.2.2 on 2023-06-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('completed', models.BooleanField()),
                ('important', models.BooleanField()),
            ],
        ),
    ]
