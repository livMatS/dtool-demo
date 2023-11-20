import os
import glob
import dtoolcore
from dtoolcore import DataSetCreator

readme_files = glob.glob('sample-content/readme/*/*.yaml')

print("Generating {:d} datasets...".format(len(readme_files)))

os.makedirs('datasets', exist_ok=True)

# generate datasets with verbose README content but mock items
for readme_file in readme_files:
    prefix, suffix = os.path.split(readme_file)
    _, name = os.path.split(prefix)
    uuid, _ = suffix.rsplit('.')

    with open(readme_file, 'r') as f:
        readme_content = f.read()

    with DataSetCreator(name, "datasets", readme_content) as ds_creator:
        for animal in ["cat", "dog", "parrot"]:
            handle = animal + ".txt"  # Unix-like relpath
            fpath = ds_creator.prepare_staging_abspath_promise(handle)
            with open(fpath, "w") as fh:
                fh.write(animal)

# copy those datasets to remote location
for dataset in dtoolcore.iter_datasets_in_base_uri('datasets'):
    dtoolcore.copy(dataset.uri, 's3://test-bucket')
