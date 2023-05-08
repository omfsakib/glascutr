# Generated by Django 4.2 on 2023-05-08 05:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('glas_cutr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('title_up', models.CharField(max_length=50)),
                ('title_down', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('button_url', models.CharField(max_length=50)),
                ('button_name', models.CharField(max_length=50)),
                ('cover_image', models.ImageField(upload_to='images/home_cover', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
