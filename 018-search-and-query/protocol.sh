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
