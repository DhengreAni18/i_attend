# Generated by Django 2.2.4 on 2019-09-02 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_auto_20190902_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='date_added',
            new_name='count_added',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 9, 2, 20, 9, 8, 396242)),
        ),
    ]
