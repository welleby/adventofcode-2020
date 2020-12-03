#!/bin/bash

if [ ! -d "./${1}" ]; then
    mkdir ./${1}
fi

cookies=dfb999220ce0ca8fe88587d0193dd18317884f7a456c34c08fbc4fdf1f9616c0ebe5ebdaa5300256a2fac3eeaba11c27871ceebcaa6e4dd7d0a751ae9bba711960569206d693ef3c515bcc4fe397be3058d3aa8f63d7615eb18ec188ce31c8c91c204d0ef388a0d252631b3072e2716c39585548d3bbb87d2698ed9395671aab24583a028258788c959ca05c044a8523cf7f728bcd145f683f44efcb48b6816bf8a60d2acc3219e60cba9cb04b5f59285a0644819be4acb71ec39838c063a39c
curl 'https://adventofcode.com/2020/day/'${1}'/input' \
  -H "${cookies}" \
  --compressed -s > ./${1}/input.txt