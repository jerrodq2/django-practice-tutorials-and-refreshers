# Generated by Django 2.0.4 on 2018-05-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100)),
                ('last', models.CharField(blank=True, max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('summary', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]