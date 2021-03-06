# -*- coding: utf-8 -*-


from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=200)),
                ('api_region', models.CharField(default=b'US', max_length=2, choices=[(b'US', b'USA'), (b'FR', b'France'), (b'CN', b'China'), (
                    b'UK', b'England'), (b'CA', b'Canada'), (b'DE', b'Germany'), (b'JP', b'Japan'), (b'IT', b'Italy'), (b'ES', b'Spain')])),
                ('user', models.OneToOneField(
                    to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
        ),
    ]
