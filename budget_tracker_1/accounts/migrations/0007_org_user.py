# Generated by Django 3.0 on 2020-01-07 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191229_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('c_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('e_file_1', models.FileField(default='Org_User_Data_1.xlsx', upload_to='uploads/')),
                ('e_file_2', models.FileField(default='Org_User_Data_2.xlsx', upload_to='uploads/')),
                ('e_file_3', models.FileField(default='Org_User_Data_3.xlsx', upload_to='uploads/')),
                ('e_file_4', models.FileField(default='Org_User_Data_4.xlsx', upload_to='uploads/')),
            ],
        ),
    ]
