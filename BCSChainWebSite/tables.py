import django_tables2 as tables
from .models import Block


class BlockTable(tables.Table):
    class Meta:
        model = Block
        template_name = "django_tables2/bootstrap.html"
        fields = ("height", "hash", "timestamp", "miner", "transactions_num",)
