# Generated by Django 5.1.2 on 2024-11-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_loan',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('Aadharno', models.IntegerField(primary_key='Aadharno', serialize=False)),
                ('DoB', models.DateField()),
                ('Address', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
