# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('actID', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20, blank=True)),
                ('content', models.CharField(max_length=100, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('is_end', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='author_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Describe',
            fields=[
                ('dscrbID', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=20, blank=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hope',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home', models.CharField(max_length=50, blank=True)),
                ('goal', models.CharField(max_length=50, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('price', models.IntegerField(null=True, blank=True)),
                ('busy', models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\xa9\xba\xe9\x97\xb2', choices=[(1, b'\xe5\xbf\x99\xe7\xa2\x8c'), (0, b'\xe7\xa9\xba\xe9\x97\xb2')])),
                ('landtype', models.CharField(default=b'any', max_length=10, verbose_name=b'\xe7\x9b\xae\xe7\x9a\x84\xe5\x9c\xb0\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'any', b'\xe9\x9a\x8f\xe6\x84\x8f'), (b'plain', b'\xe5\xb9\xb3\xe5\x8e\x9f'), (b'mountain', b'\xe5\xb1\xb1\xe6\x9e\x97'), (b'water', b'\xe6\xb9\x96\xe6\xb5\xb7'), (b'interest', b'\xe5\x90\x8d\xe8\x83\x9c'), (b'scenery', b'\xe6\x99\xaf\xe5\x8c\xba'), (b'explore', b'\xe6\x8e\xa2\xe9\x99\xa9')])),
                ('hopesry', models.CharField(max_length=50, blank=True)),
                ('is_commit', models.BooleanField(default=False)),
                ('tip', models.CharField(max_length=128, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('logID', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\x97\xa5\xe5\xbf\x97\xe9\xa2\x98\xe7\x9b\xae')),
                ('content', models.CharField(max_length=1000, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('is_img', models.BooleanField(default=False)),
                ('img_name', models.CharField(default=b'', max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LogImg',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20, blank=True)),
                ('log', models.ForeignKey(to='myapp.Log')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('msgID', models.AutoField(serialize=False, primary_key=True)),
                ('msg_type', models.IntegerField()),
                ('msg_deal', models.IntegerField(default=3)),
                ('is_req', models.BooleanField()),
                ('is_read', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('come', models.ForeignKey(related_name='come_set', to=settings.AUTH_USER_MODEL)),
                ('go', models.ForeignKey(related_name='go_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('act', models.ForeignKey(related_name='person_set', to='myapp.Activity')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=16, blank=True)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.IntegerField(default=1, choices=[(1, b'\xe7\x94\xb7'), (0, b'\xe5\xa5\xb3')])),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('qq', models.CharField(max_length=20, blank=True)),
                ('travellike', models.CharField(max_length=50, blank=True)),
                ('question', models.CharField(max_length=50, blank=True)),
                ('answer', models.CharField(max_length=50, blank=True)),
                ('is_img', models.IntegerField(default=0)),
                ('friend', models.ManyToManyField(related_name='_friend_+', to='myapp.Profile')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('siteID', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe6\x99\xaf\xe7\x82\xb9\xe5\x90\x8d')),
                ('content', models.CharField(max_length=50, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('price', models.IntegerField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('is_img', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SiteCommit',
            fields=[
                ('scID', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('site', models.ForeignKey(related_name='site_sitecommit_set', to='myapp.Site')),
                ('user', models.ForeignKey(related_name='user_sitecommit_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SiteImg',
            fields=[
                ('siteID', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20, blank=True)),
                ('site', models.ForeignKey(to='myapp.Site')),
            ],
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('strgyID', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('site', models.ForeignKey(related_name='site_strgy_set', blank=True, to='myapp.Site', null=True)),
                ('user', models.ForeignKey(related_name='user_strgy_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
