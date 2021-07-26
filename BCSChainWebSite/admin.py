from django.contrib import admin
from .models import Block


class BlockAdmin(admin.ModelAdmin):
    list_display = ("height", "hash", "timestamp", "miner", "transactions_num",)
    list_editable = ("hash", "timestamp", "miner", "transactions_num",)

admin.site.register(Block, BlockAdmin)
