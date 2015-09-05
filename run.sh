#!/bin/sh

cat data/tree-felling-list.csv | python src/clean.py | python src/geocode.py | python src/mapboxify.py
