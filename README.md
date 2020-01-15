# Kindle Highlights Extractor

> Requirements: Docker

```khex.sh``` will extract highlights from a locally mounted Kindle, store the hightlights in a timestamped JSON
under ```highlights/```, display any highlights that are new since the previous run, and store the new highlights in
```./new_highlights.txt```.

```khex.sh``` appends a footer to each highlight, useful for adding tags or other boilerplate.

## Usage
> Optional: Edit FOOTER in parse.py

    ./khex.sh


### Development
    docker build -t khex .
    docker run --name hl --rm -v`pwd`/app:/app \
                              -v`pwd`/clippings:/clippings \
                              -v`pwd`/highlights:/highlights \
                              --entrypoint bash -ti khex
