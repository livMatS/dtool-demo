#!/bin/bash -x
dtool create demo-dataset

echo test-content > test-data

dtool add item test-data demo-dataset

dtool readme interactive demo-dataset

dtool add metadata demo-dataset test-data purpose testing

dtool freeze demo-dataset

dtool overlays show demo-dataset

dtool verify demo-dataset

echo "addition" >> demo-dataset/data/test-data

dtool verify demo-dataset

