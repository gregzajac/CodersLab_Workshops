# Generated by Django 2.2.7 on 2020-02-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactbox', '0003_auto_20200213_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('persons', models.ManyToManyField(to='contactbox.Person')),
            ],
        ),
    ]