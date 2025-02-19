# Generated by Django 2.0.2 on 2018-11-01 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('AccountNumber', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Balance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BankUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=10)),
                ('EmailID', models.EmailField(max_length=70)),
                ('address', models.CharField(max_length=250)),
                ('otp_value', models.CharField(default='0', editable=False, max_length=16)),
                ('type_of_user', models.CharField(choices=[('R', 'Regular Employee'), ('S', 'System Manager'), ('A', 'Admin'), ('I', 'Individual Customer'), ('O', 'Organization')], max_length=1)),
                ('publicKey', models.CharField(default='0', max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='keyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=10000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SecureBank.BankUser')),
            ],
        ),
        migrations.CreateModel(
            name='LoggedInUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, max_length=32, null=True)),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logged_in_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileEditRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newEmail', models.EmailField(max_length=70)),
                ('Status', models.CharField(choices=[('A', 'Approval required'), ('P', 'Processed'), ('R', 'Rejected'), ('E', 'Unsuccessful')], editable=False, max_length=1)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SecureBank.BankUser')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField(default=0, editable=False)),
                ('Status', models.CharField(choices=[('O', 'OTP required'), ('A', 'Approval required'), ('P', 'Processed'), ('R', 'Rejected'), ('E', 'Unsuccessful')], editable=False, max_length=1)),
                ('Type', models.CharField(choices=[('C', 'Credit'), ('D', 'Debit'), ('T', 'Transfer')], default='T', editable=False, max_length=1)),
                ('CreationTime', models.DateTimeField(auto_now_add=True)),
                ('Employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SecureBank.BankUser')),
                ('FromAccount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='FromAccount', to='SecureBank.Account')),
                ('ToAccount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ToAccount', to='SecureBank.Account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='AccountHolder',
            field=models.ForeignKey(null=True, on_delete=True, to='SecureBank.BankUser'),
        ),
    ]
