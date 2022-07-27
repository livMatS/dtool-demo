# place dtool config in home folder
cat dtool.json
mkdir -p ~/.config/dtool
cp dtool.json ~/.config/dtool/

source ../005-setup/venv/bin/activate

# isnpect local base URI
dtool ls -v ../010-dataset-creation

# inspect remote base URI
dtool ls -v s3://test-bucket

# copy from local to remote
dtool cp ../010-dataset-creation s3://test-bucket

# inspect remote base URI
dtool ls -v s3://test-bucket
