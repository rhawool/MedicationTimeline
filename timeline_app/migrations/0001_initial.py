# Generated by Django 4.1.3 on 2022-11-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntakeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intake_time', models.CharField(max_length=50)),
                ('medicine_name', models.CharField(max_length=50)),
            ],
        ),
    ]