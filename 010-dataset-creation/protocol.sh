#!/bin/bash -x
dtool create 20211027-demo-dataset

echo test-content > test-data

dtool add item test-data 20211027-demo-dataset

dtool readme interactive 20211027-demo-dataset

dtool add metadata 20211027-demo-dataset test-data purpose testing

dtool freeze 20211027-demo-dataset

dtool overlays show 20211027-demo-dataset

dtool verify 20211027-demo-dataset

echo "addition" >> 20211027-demo-dataset/data/test-data

dtool verify 20211027-demo-dataset

