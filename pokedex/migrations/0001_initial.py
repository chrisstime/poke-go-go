# Generated by Django 3.0.2 on 2020-01-15 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pokedex_number', models.IntegerField(max_length=20)),
            ],
            options={
                'ordering': ['pokedex_number'],
            },
        ),
    ]
