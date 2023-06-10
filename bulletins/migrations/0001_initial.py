# Generated by Django 4.2.1 on 2023-05-06 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bul_title', models.CharField(max_length=255)),
                ('bul_text', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=255)),
                ('bul_author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserSubscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletins.subscribers')),
                ('user_connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='subscribers',
            name='subscribers',
            field=models.ManyToManyField(through='bulletins.UserSubscribers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_text', models.TextField()),
                ('reply_date', models.DateTimeField(auto_now_add=True)),
                ('reply_bul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletins.bulletin')),
                ('reply_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
