#!/usr/bin/env python

import glob
import csv
import re
from os import path

post_dir = '_posts/'

filenames = glob.glob(post_dir + '*md')


with open('titles.csv', 'w', newline='', encoding='utf-16') as csvfile:
    fieldnames = ['date', 'title']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    posts = []
    for filename in filenames:
        f = open(filename, 'r', encoding='utf8')
        contents = f.read()

        match = re.search(r'^thumbnail_title: (.+)', contents, re.M) or re.search(r'^title: (.+)', contents, re.M)
        if match:
            title = match.group(1).replace('"', '')
            date = '-'.join(path.basename(filename).split('-')[0:3])
            posts.append({'date': date, 'title': title})
        f.close()

    posts.sort(key=lambda x: x['date'], reverse=True)
    for post in posts:
        writer.writerow(post)

