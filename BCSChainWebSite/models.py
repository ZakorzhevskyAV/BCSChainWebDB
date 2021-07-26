from django.db import models


class Block(models.Model):
    height = models.IntegerField(primary_key=True, verbose_name='height')
    hash = models.TextField(verbose_name='hash', max_length=49)
    timestamp = models.IntegerField(verbose_name='timestamp')
    miner = models.TextField(verbose_name='miner', max_length=49)
    transactions_num = models.IntegerField(verbose_name='transactions_num')

    class Meta:
        ordering = ('height',)
