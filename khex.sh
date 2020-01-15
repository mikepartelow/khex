#!/bin/bash
set -e

PATH_TO_CLIPPINGS='/Volumes/Kindle/documents/My Clippings.txt'

if [[ -f $PATH_TO_CLIPPINGS ]]
then
  docker build -t khex .
  docker run --name khex --rm -v $(dirname "$PATH_TO_CLIPPINGS"):/clippings \
                              -v `pwd`/highlights:/highlights \
                              -t khex | tee new_highlights.txt | less

else
  echo "Could not find clippings at $PATH_TO_CLIPPINGS"
fi