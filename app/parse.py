#!/usr/bin/env python3

import os
import pytz
import json
import hashlib
import datetime

highlights      = dict()
new_highlights  = []

TIMEZONE        = pytz.timezone('America/Los_Angeles')
INPATH          = '/clippings/My Clippings.txt'
OUTPATH         = '/highlights/highlights.json'

# this footer will appear after each highlight
#
FOOTER            = '#quote #highlight #book'

if os.path.exists(OUTPATH):
    with open(OUTPATH, 'rb') as f:
        highlights = json.loads(f.read().decode('utf-8'))

with open(INPATH, 'r') as f:
    index = 0
    highlight = dict()

    for line in f:
        line = line.strip()

        if index == 0:
            highlight['book'] = line
        elif index == 1:
            what, added = line.rsplit('|', 1)
            if 'Highlight' in what:
                dt = datetime.datetime.strptime(added.split(',', 1)[1], ' %B %d, %Y %I:%M:%S %p')
                highlight['added'] = dt.isoformat()
        elif index == 2:
            pass
        elif index == 3:
            highlight['text'] = line
        elif index == 4:
            text = highlight['text']
            if 'added' in highlight and text:
                hash = hashlib.blake2b(text.encode('utf-8')).hexdigest()

                if not hash in highlights:
                    highlight['footer'] = FOOTER
                    highlights[hash] = highlight
                    new_highlights.append(highlight)

            highlight = dict()
            index = -1

        index += 1

for highlight in sorted(new_highlights, key=lambda h: h['added']):
    print("{text}\n\n{book}\n\n{added}\n\n{footer}\n==========".format(**highlight))

if new_highlights:
    localtime = datetime.datetime.now().replace(tzinfo=pytz.utc).astimezone(TIMEZONE)
    timestamp = localtime.strftime("%Y%m%d_%H%M%S")
    timestamped_outpath = "{}.{}".format(OUTPATH, timestamp)

    with open(timestamped_outpath, 'wb') as f:
        f.write(json.dumps(highlights).encode('utf-8'))

    with open(OUTPATH, 'wb') as f:
        f.write(json.dumps(highlights).encode('utf-8'))
