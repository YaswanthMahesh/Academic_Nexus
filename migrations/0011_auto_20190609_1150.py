# Generated by Django 2.2.2 on 2019-06-09 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0010_auto_20190609_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mocktest1',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='onlineapp.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineapp.College'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineapp.College'),
        ),
    ]
