import sys
import ssl
import time
import asyncio
import argparse
import websockets

async def test_me():
    print('i am working yes ....')

test_me()


top_parser = argparse.ArgumentParser(description=' File from me -----')
args = top_parser.parse_args()

asyncio.get_event_loop().run_until_complete(test_me())