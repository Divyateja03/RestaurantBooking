# Generated by Django 5.0.6 on 2024-05-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Descrption', models.TextField(max_length=500)),
                ('servesPeople', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=5, max_digits=5)),
                ('preparationTime', models.IntegerField()),
                ('image', models.ImageField(upload_to='booking/')),
            ],
        ),
    ]