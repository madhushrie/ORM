# Generated by Django 5.1.2 on 2024-10-28 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankloan',
            fields=[
                ('name', models.CharField(max_length=15)),
                ('phoneno', models.IntegerField()),
                ('accountno', models.IntegerField(primary_key='accountno', serialize=False)),
                ('loan_amount', models.IntegerField()),
                ('interset', models.FloatField()),
            ],
        ),
    ]