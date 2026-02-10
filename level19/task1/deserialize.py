import json
import os
from datetime import datetime

def custom_decoder(dct):
    if 'timestamp' in dct: dct['timestamp'] = datetime.fromisoformat(dct['timestamp'])
    return dct

transaction_list = None

if os.path.exists('transaction_list.json'):
    # Десериализация с пользовательским декодером
    with open("transaction_list.json", "r") as file:
        transaction_list = json.load(file, object_hook=custom_decoder)


