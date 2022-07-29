# copy dtool config
cat dtool.json

mkdir -p ~/.config/dtool

cp dtool.json ~/.config/dtool

# clear text search
dtool search demo

# inspect README content
dtool readme show s3://test-bucket/07c2cae6-7611-4918-a10b-2bc24a365970

# structured query
dtool query '{"readme.owners.name":{"$regex":"H.*rmann"}}'

# edit README content
dtool readme edit s3://test-bucket/1a1f9fad-8589-413e-9602-5bbd66bfe675
# i.e. modify the owner's name in the README

# another structured query
dtool query '{"readme.owners.name":{"$regex":"H.*rmann"}}'
