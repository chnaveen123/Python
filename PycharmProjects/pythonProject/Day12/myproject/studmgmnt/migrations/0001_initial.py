# Generated by Django 4.0.4 on 2022-04-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=50)),
                ('stud_dob', models.CharField(max_length=20)),
                ('stud_class', models.CharField(max_length=30)),
            ],
        ),
    ]