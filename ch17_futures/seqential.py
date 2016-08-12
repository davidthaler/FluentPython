# Example 17-2 from Fluent Python

import os
import sys
import time

import requests

# Apparently this is an OK call to str.split
CC = ('CN IN US ID BR PK NG BD RU JP '
     'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'downloads'

def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def download_many(cc_list):
    for cc in sorted(cc_list):
        img = get_flag(cc)
        show(cc)
        save_flag(img, cc.lower() + '.gif')
    return len(cc_list)

def main(download_many):
    t0 = time.time()
    ct = download_many(CC)
    et = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f} seconds'
    print(msg.format(ct, et))

if __name__ == '__main__':
    main(download_many)
