#!/usr/bin/env bash

for i in day*; do
	echo $i
	cd $i
	./build.sh
	cd ..
done
