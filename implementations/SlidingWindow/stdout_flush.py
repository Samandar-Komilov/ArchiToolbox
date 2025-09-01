import sys
import time

def moving_words(text, delay=0.5):
    for i in range(len(text)):
        sys.stdout.write('\r' + text[i:] + text[:i])
        sys.stdout.flush()
        time.sleep(delay)

moving_words('hello world')