# Generated by Django 2.2.2 on 2019-06-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0002_college_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateTimeField(max_length=10)),
                ('college', models.CharField(max_length=20)),
                ('drop_out', models.BooleanField()),
            ],
        ),
    ]