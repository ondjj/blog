# Generated by Django 2.2.2 on 2022-02-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20220209_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('albums', models.ManyToManyField(to='photo.Album')),
            ],
        ),
    ]
