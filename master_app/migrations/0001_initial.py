# Generated by Django 3.2.9 on 2021-11-12 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Student Info',
            },
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tcr_name', models.CharField(max_length=30)),
                ('tcr_sname', models.CharField(max_length=30)),
                ('tcr_std', models.ManyToManyField(to='master_app.StudentInfo')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(default='H. Aliyev str.', max_length=40)),
                ('home_address', models.CharField(max_length=40)),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_app.studentinfo')),
            ],
            options={
                'verbose_name_plural': 'Student Address',
            },
        ),
    ]
