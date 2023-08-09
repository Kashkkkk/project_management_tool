# Generated by Django 2.2 on 2019-04-24 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('employees', '0006_auto_20190424_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Branch'),
        ),
        migrations.AddField(
            model_name='employees',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.Designation'),
        ),
        migrations.AddField(
            model_name='employees',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='joining date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='leaves',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='employees',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
