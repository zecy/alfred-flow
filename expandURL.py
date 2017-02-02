#! /usr/local/bin/python3

import re
import sys

input = sys.argv[1].split(" ")

if (len(input) == 2):

    count = input[0]
    url   = input[1]

    if(re.search("nhentai", url)):
        pat     = re.compile(r"https://t.nhentai.net/galleries/(\d+)/\d+t.(jpg|png)")
        comicId = re.search(pat, url).group(1) 
        imgType = re.search(pat, url).group(2) 
        linkPre = "https://i.nhentai.net/galleries/"
        links   = []
        for i in range(int(count)):
            link = linkPre + comicId + '/' + str(i + 1) + '.' + imgType
            links.append(link)
        out = '\n'.join(links)
    else:
        out = "url"
else:
        out = "argument"

sys.stdout.write(out)