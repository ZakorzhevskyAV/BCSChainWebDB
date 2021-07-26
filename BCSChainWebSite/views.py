from .models import Block
from django.shortcuts import render
from .tables import BlockTable


def index(request):
    if request.method == 'GET':
        block_set = Block.objects.all().order_by('-height')
        table = BlockTable(block_set)
        table.paginate(page=request.GET.get("page", 1), per_page=100)
        return render(request, 'index.html', {'table': table})


def block_page(request, block_height=None):
    if request.method == 'GET':
        block_object = Block.objects.filter(height=block_height)
        table = BlockTable(block_object)
        return render(request, 'index.html', {'table': table})
