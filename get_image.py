# -*- coding: utf-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup
import argparse
import sys

def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Get arguments')
    parser.add_argument('--url', dest='url',
                        help='Download source url',
                        default=0, type=str)
    parser.add_argument('--output', dest='save_path',
                        help='image save path',
                        default=None, type=str)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args

args = parse_args()
url = args.url
print('url=',url)
res = requests.get(url)
soup = BeautifulSoup(res.text , 'html.parser')
pic_list = soup.select('.item_box .post a img')
print('pic_list=',pic_list)
i = 0
for img_url in pic_list:
    url_list = img_url['src']
    print('url_list=',url_list)
    save_path = args.save_path + '/' + str(i) + '.jpg'
    print('save_path=',save_path)
    pic_file = urllib.urlopen(url_list).read()
    f = open(save_path, "wb")
    f.write(pic_file)
    f.close()
    i = i+1
