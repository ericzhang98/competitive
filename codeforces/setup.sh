#!/bin/bash

echo Setting up files
for c in {a..f}
do
    if [ -f $c.cpp ]; then
        echo $c.cpp exists
    else
        echo Creating $c.cpp
        cp template_cpp.cpp $c.cpp
    fi
done
for c in {a..f}
do
    if [ -f test_$c ]; then
        echo test_$c exists
    else
        echo Creating test_$c
        touch test_$c
    fi
done
