# Generated by Django 4.1 on 2022-10-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuName', models.TextField()),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]