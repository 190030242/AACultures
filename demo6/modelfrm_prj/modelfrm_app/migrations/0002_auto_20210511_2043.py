# Generated by Django 3.1.7 on 2021-05-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelfrm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userreg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aadhar', models.IntegerField(max_length=12)),
                ('Name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
        migrations.DeleteModel(
            name='GeeksModel',
        ),
    ]