#!/usr/bin/env python

import glob
import csv
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
        crawl = False
        for line in f:
            if crawl:
                current_tags = line.strip().split(" ", 1)
                if current_tags[0] == 'title:':
                    title = current_tags[1].replace('"', '')
                    date = '-'.join(path.basename(filename).split('-')[0:3])
                    posts.append({'date': date, 'title': title})

                    crawl = False
                    break
            if line.strip() == '---':
                if not crawl:
                    crawl = True
                else:
                    crawl = False
                    break
        f.close()

    posts.sort(key=lambda x: x['date'])
    for post in posts:
        writer.writerow(post)

