# Generated by Django 2.2.7 on 2020-02-13 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactbox', '0002_auto_20200213_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
