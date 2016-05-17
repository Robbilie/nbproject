# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20160329_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='ensemble',
            name='default_pause',
            field=models.BooleanField(default=False, verbose_name=b'Pause on staff Video comments by default'),
        ),
        migrations.AddField(
            model_name='location',
            name='pause',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='assignmentgrade',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 14, 39, 13, 743300)),
        ),
        migrations.AlterField(
            model_name='assignmentgradehistory',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 14, 39, 13, 745423)),
        ),
        migrations.AlterField(
            model_name='commentlabel',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 14, 39, 13, 747807)),
        ),
        migrations.AlterField(
            model_name='commentlabelhistory',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 14, 39, 13, 748670)),
        ),
        migrations.AlterField(
            model_name='filedownload',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 14, 39, 13, 740312)),
        ),
        migrations.AlterField(
            model_name='guesthistory',
            name='t_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 14, 39, 13, 741733), null=True),
        ),
        migrations.AlterField(
            model_name='guestloginhistory',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 14, 39, 13, 742494), null=True),
        ),
        migrations.AlterField(
            model_name='invite',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 14, 39, 13, 718220), null=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='atime',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 14, 39, 13, 741121), null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 17, 14, 39, 13, 723147), null=True),
        ),
    ]
