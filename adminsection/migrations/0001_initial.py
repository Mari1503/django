# Generated by Django 2.2 on 2020-01-19 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('PhoneNumber', models.CharField(max_length=11)),
                ('Gender', models.CharField(max_length=11)),
                ('Note', models.TextField()),
                ('CreateDate', models.DateTimeField(auto_now_add=True)),
                ('UpdateDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=25)),
                ('Cost', models.PositiveIntegerField()),
                ('TimeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Note', models.TextField()),
                ('Catagories', models.ManyToManyField(to='adminsection.Service')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminsection.Customer')),
            ],
        ),
    ]