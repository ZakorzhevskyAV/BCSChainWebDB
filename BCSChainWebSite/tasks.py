import requests
import json
from .models import Block
from background_task import background


@background(schedule=5)
def blockchain_update():
    blockchain_info = requests.get('https://bcschain.info/api/info')
    blockchain_json = json.loads(blockchain_info.text)
    blockchain_height = blockchain_json['height']
    for block_height in range(1, blockchain_height+1):
        if Block.objects.filter(height=block_height).count() == 0:
            block_info = requests.get(f'https://bcschain.info/api/block/{block_height}')
            block_json = json.loads(block_info.text)
            b = Block.objects.create(
                height=block_json['height'],
                hash=block_json['hash'],
                timestamp=block_json['timestamp'],
                miner=block_json['miner'],
                transactions_num=len(block_json['transactions']),
            )
            b.save()
