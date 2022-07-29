# place dtool config in home folder
cat dtool.json
mkdir -p ~/.config/dtool
cp dtool.json ~/.config/dtool/

source ../005-setup/venv/bin/activate

# inspect remote base URIs
dtool ls s3://test-bucket
dtool ls -v s3://test-bucket

# inspect remote dataset
dtool ls -v s3://test-bucket/1a1f9fad-8589-413e-9602-5bbd66bfe675
dtool summary s3://test-bucket/1a1f9fad-8589-413e-9602-5bbd66bfe675

# create local base URI
mkdir -p datasets

# copy dataset from remote to local
dtool cp s3://test-bucket/1a1f9fad-8589-413e-9602-5bbd66bfe675 datasets

# inspect local dataset
dtool ls -v datasets
dtool summary datasets/simple_test_dataset
