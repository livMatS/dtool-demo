#!/bin/bash -x
# create README.yml template with simple metadata ontology
cat dtool_readme_template.yml
cp .dtool_readme.yml

# create simple dtool.json configuration
cat dtool.json
mkdir -p ~/.config/dtool
cp dtool.json ~/.config/dtool/

# create and freeze dataset with one item
dtool create demo-dataset
echo test-content > test-data-file.txt
dtool add item test-data-file.txt demo-dataset
dtool readme interactive demo-dataset
dtool freeze demo-dataset

# gather info
dtool ls .
dtool ls -v .

dtool ls demo-dataset
dtool ls -v demo-dataset

dtool summary demo-dataset
dtool summary -f json demo-dataset

dtool verify demo-dataset
echo "illegal-addition" >> demo-dataset/data/test-data-file.txt
dtool verify demo-dataset

