# Generated by Django 3.2.9 on 2021-12-25 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_app', '0010_bloggg'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bloggg',
        ),
        migrations.AddField(
            model_name='blogname',
            name='surrname',
            field=models.CharField(default=255, max_length=55),
            preserve_default=False,
        ),
    ]