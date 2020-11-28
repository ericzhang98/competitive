#!/bin/bash

folder=$1
templates=templates

if [ -z "$1" ]; then
  echo "No folder name provided, exiting..."
  exit 1
fi
if [ -d $folder ]; then
  echo "$folder already exists, exiting..."
  exit 1
fi

echo "Setting up files in $folder"
mkdir $folder
cp $templates/Makefile $folder
for c in {a..f}
do
  if [ -f $folder/$c.cpp ]; then
    echo "$folder/$c.cpp exists"
  else
    echo "Creating $folder/$c.cpp"
    cp $templates/cpp.cpp $folder/$c.cpp
  fi
done
for c in {a..f}
do
  if [ -f $folder/test_$c ]; then
    echo "$folder/test_$c exists"
  else
    echo "Creating $folder/test_$c"
    touch $folder/test_$c
  fi
done
