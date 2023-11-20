# snippet used to extract README.yml content from true datasets on a dtool lookup server
import dtool_lookup_api.asynchronous as dl

import os
import pprint
import ruamel.yaml as yaml

uuid = '88c14189-f072-4df0-a04b-57bf27760b9d'

res = await dl.by_uuid(uuid)

print("Lookup result for uuid {uuid:}:".format(uuid=uuid))
pprint.pprint(res)

res = await dl.graph(uuid)
print("Graph lookup result for uuid {uuid:}:".format(uuid=uuid))
pprint.pprint(res)

# store readme content in readme/{DATASET_NAME}/{UUID}.yaml files
os.makedirs('readme', exist_ok=True)
for metadata_info in res:
    readme_content = await dl.readme(metadata_info['uri'])
    outdir = os.path.join('readme', metadata_info["name"])
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir,metadata_info["uuid"] + '.yaml')
    with open(outfile, 'w') as f:
        yaml.dump(readme_content, f, allow_unicode=True)
