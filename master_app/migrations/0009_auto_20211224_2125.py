# Generated by Django 3.2.9 on 2021-12-24 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_app', '0008_blogtext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherinfo',
            name='tcr_std',
        ),
        migrations.DeleteModel(
            name='StudentAddress',
        ),
        migrations.DeleteModel(
            name='StudentInfo',
        ),
        migrations.DeleteModel(
            name='TeacherInfo',
        ),
    ]