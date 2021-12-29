# Generated by Django 4.0 on 2021-12-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FromDetails',
            fields=[
                ('usn', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('stream', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'FromDetails',
                'verbose_name_plural': 'FromDetailss',
            },
        ),
    ]
