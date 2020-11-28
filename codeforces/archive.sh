#!/bin/bash

archive=$1
if [ -z "$1" ]; then
  echo "no argument supplied"
fi
if [ -d $archive ]; then
    echo "$archive folder already exists, exiting..."
    exit
fi

echo creating archive folder
mkdir $archive
for c in {a..f}
do
    if [ -f $c.cpp ]; then
        echo "moving $c.cpp to $archive"
        mv $c.cpp $archive
    fi
done
for c in {a..f}
do
    if [ -f test_$c ]; then
        echo "moving test_$c to $archive"
        mv test_$c $archive
    fi
done

