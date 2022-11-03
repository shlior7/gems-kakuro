#!/bin/bash

sudo -n dnf install -y cmake

cd api/kakuro
rm -rf dist
mkdir dist
cd dist
cmake ..
make
