# Generated by Django 2.2.6 on 2019-10-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(default='noname', max_length=100, verbose_name='CoueseName')),
                ('Cid', models.CharField(default='noname', max_length=100, verbose_name='Cid')),
            ],
        ),
    ]
