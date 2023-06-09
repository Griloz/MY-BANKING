import logging


logging.basicConfig(
    filename=r'.\logs\june04_2023.log',
    encoding='utf-8',
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

logger = logging.getLogger()
