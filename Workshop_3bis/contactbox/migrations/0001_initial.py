# Generated by Django 2.2.7 on 2020-02-13 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=128)),
                ('block_number', models.CharField(max_length=32)),
                ('flat_number', models.CharField(max_length=32, null=True)),
                ('post_code', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('email_type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=32)),
                ('phone_type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactbox.Address')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactbox.Email')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactbox.Phone')),
            ],
        ),
    ]
