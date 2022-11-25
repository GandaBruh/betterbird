# Generated by Django 4.1.2 on 2022-11-21 15:38

import ckeditor.fields
import datetime
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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=9999)),
                ('introduction', models.CharField(max_length=9999)),
                ('tag', models.CharField(max_length=9999)),
                ('detail', ckeditor.fields.RichTextField()),
                ('tag1', models.BooleanField(default=False)),
                ('tag2', models.BooleanField(default=False)),
                ('tag3', models.BooleanField(default=False)),
                ('tag4', models.BooleanField(default=False)),
                ('tag5', models.BooleanField(default=False)),
                ('tag6', models.BooleanField(default=False)),
                ('tag7', models.BooleanField(default=False)),
                ('date1', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='users/static/images')),
                ('donate', models.IntegerField(default=0)),
                ('blogType', models.IntegerField(default=0)),
                ('recommended', models.BooleanField(default=False)),
                ('like', models.IntegerField(default=0)),
                ('expectCookies', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CookieCoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField(default=0)),
                ('slip', models.CharField(blank=True, max_length=9999, null=True)),
                ('title', models.CharField(default='', max_length=9999)),
                ('transactionCode', models.CharField(max_length=9999)),
                ('historyType', models.BooleanField(default=False)),
                ('currency', models.BooleanField(default=False)),
                ('date', models.DateTimeField(null=True)),
                ('time', models.TimeField(default=datetime.time(16, 0))),
                ('cookie', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balanceCookie', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ViewBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReportBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason1', models.BooleanField(default=False, verbose_name='reason1')),
                ('reason2', models.BooleanField(default=False, verbose_name='reason2')),
                ('reason3', models.BooleanField(default=False, verbose_name='reason3')),
                ('reason4', models.BooleanField(default=False, verbose_name='reason4')),
                ('reason5', models.BooleanField(default=False, verbose_name='reason5')),
                ('reason6', models.BooleanField(default=False, verbose_name='reason6')),
                ('otherReason', models.CharField(max_length=256)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OwnedBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=5000)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='users/static/images')),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=9999)),
                ('country', models.CharField(max_length=9999)),
                ('likeCount', models.IntegerField(default=0)),
                ('viewCount', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgName', models.CharField(default='1', max_length=9999)),
                ('image', models.ImageField(default='', upload_to='users/static/images')),
                ('foundingDay', models.DateField()),
                ('phone', models.CharField(max_length=9999)),
                ('address', models.CharField(max_length=9999)),
                ('country', models.CharField(max_length=9999)),
                ('likeCount', models.IntegerField(default=0)),
                ('viewCount', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=9999)),
                ('phone', models.CharField(max_length=9999)),
                ('tag', models.CharField(max_length=9999)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
