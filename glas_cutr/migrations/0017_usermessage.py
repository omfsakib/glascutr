# Generated by Django 4.2 on 2023-05-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glas_cutr', '0016_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
