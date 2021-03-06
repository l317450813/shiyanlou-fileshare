# Generated by Django 2.1.8 on 2020-06-19 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downloadcount', models.IntegerField(default=0, verbose_name='访问次数')),
                ('code', models.CharField(max_length=8, verbose_name='code')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2020, 6, 19, 17, 21, 28, 700085), verbose_name='上传时间')),
                ('path', models.CharField(max_length=64, verbose_name='存储路径')),
                ('name', models.CharField(max_length=32, verbose_name='文件名')),
                ('filesize', models.CharField(max_length=8, verbose_name='文件大小')),
                ('pcip', models.CharField(max_length=16, verbose_name='IP 地址')),
            ],
        ),
    ]
