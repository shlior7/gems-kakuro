#!/bin/bash

cd api/kakuro
rm -rf dist
mkdir dist
cd dist
cmake ..
make
