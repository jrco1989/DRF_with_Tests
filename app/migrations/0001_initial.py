# Generated by Django 3.2.5 on 2021-07-29 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('userId', models.IntegerField(verbose_name='post user id')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='post id')),
                ('title', models.CharField(max_length=200, verbose_name='post title')),
                ('body', models.TextField(verbose_name='post body')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['id'],
            },
        ),
    ]
