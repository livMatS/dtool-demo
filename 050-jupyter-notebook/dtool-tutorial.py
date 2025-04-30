# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # dtool tutorial
#

# %% [markdown]
# For a thorough documentation on how to work with datasets via dtool's Python API dtoolcore, see https://dtoolcore.readthedocs.io.

# %% [markdown]
# ## Setup

# %% [markdown]
# Copy the `dtool.json` config file within this folder into `~/.config/dtool/dtool.json`, e.g. with
#
# ```bash
# mkdir -p ~/.config/dtool
# cp dtool.json ~/.config/dtool
# ```
#
# Create a virtual environment with the neccessary dtool packages and jupyter with
#
# ```bash
# python -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# ```
#
# and launch the jupyter notebook server with
#
# ```bash
# jupyter notebook
# ```

# %% [markdown]
# ## Copy dataset from remote storage backend
# Import dtoolcore and os

# %%
import dtoolcore, os
import time
from datetime import datetime
import yaml

# %% [markdown]
# In this example, we get a file from demo.dtool.dev, which we configured in the dtool.jeson of our `setup`:

# %%
# URI of the remote dataset you want to copy
# this is a random example dataset from https://demo.dtool.dev/
remote = "s3://test-bucket/"
remote_uri = "s3://test-bucket/1a1f9fad-8589-413e-9602-5bbd66bfe675"
# generate unique timestamp
# timestamp = str(datetime.fromtimestamp(int(time.time())))
timestamp = str(time.time())

# Local destination where you want to copy the dataset
current_dir = os.getcwd()
data_dir = current_dir+"/"+ timestamp +"_test_dataset"

os.makedirs(data_dir, exist_ok=True)

# Copy the dataset
dtoolcore.copy(remote_uri, data_dir)

# %% [markdown]
# Now we can see the copyed data from the s3 remote storage with

# %% jupyter={"outputs_hidden": true}
# %ls -R

# %% [markdown]
# ## Create local dataset

# %% [markdown]
# Create a proto dataset
#
# todo:
# - dtool create demo-dataset
# - echo test_content >> testfile
# - dtool add item testfile demo-dataset
# - add metadata to readme
# - freeze
# - cat Annot and tree dataset, use different ls
# - try to add after freezing

# %%
timestamp = str(time.time())
current_dir = os.getcwd()
data_dir2 = os.path.join(current_dir,timestamp+"_data")

os.makedirs(data_dir2, exist_ok=True)

#with open(os.path.join(data_dir2,"jupyter_test_file.txt"), "w") as f:
with open("jupyter_test_file.txt", "w") as f:
    f.write("This is a test file")

new_dataset = dtoolcore.create_proto_dataset(
    name="my-dataset",
    base_uri=data_dir2
)

# %% [markdown]
# Add an item to the dataset

# %%
# %ls -R

# %%
new_dataset.put_item( "jupyter_test_file.txt", "jupyter_test_file.txt")

# %% [markdown]
# Add metadata

# %%
readme = yaml.dump(    dict(
        description="For demonstation purposes only",
        project="Today's test project.",
        author="Johannes Laurin Hoermann",
        username="jotelha",
        orcid="0000-0001-5867-695X",
        organization="University of Freiburg",
        program="Haushaltsstelle"
    ))
new_dataset.put_readme(readme)

# %%
# Freeze the dataset
new_dataset.freeze()

# %% [markdown]
# Check the contents and validate

# %%
# !tree {data_dir2}

# %% [markdown]
# Show metadata of dataset

# %%
print(new_dataset.get_readme_content(),
      new_dataset.name, "\n", new_dataset.uri,"\n", new_dataset.uuid )
#proto_dataset.

# %%
manifest2 = new_dataset.generate_manifest()
manifest2['items'].items()

# %% [markdown]
# Try to add another file after freezing the dataset

# %%
with open("another_jupyter_test_file.txt", "w") as f:
    f.write("This is another test file")

new_dataset.put_item( "another_jupyter_test_file.txt", "another_jupyter_test_file.txt")

# %%
# !tree {data_dir2}

# %%
# freeze dataset a second time?
new_dataset.freeze()

# %% [markdown]
# ## Copy dataset to remote storage backend

# %%
# URI of the remote dataset you want to copy
remote = "s3://test-bucket/"

timestamp = str(time.time())
data_dir2 = current_dir+"/"+ timestamp +"_data"

if not os.path.exists(data_dir2):
    os.mkdir(data_dir2)

with open(data_dir2+"/jupyter_test_file.txt", 'w') as f:
    f.write("This is a test file")

another_dataset = dtoolcore.create_proto_dataset(
    name="my-dataset",
    base_uri=data_dir2
)

another_dataset.freeze()

# Copy the dataset to S3
dtoolcore.copy(another_dataset.uri, remote+another_dataset.uuid)


# %% [markdown]
# ## Search and query entries on dserver

# %% [markdown]
# See documentation of dtool-lookup-api at https://dtool-lookup-api.readthedocs.io for a thorough documentation of posing queries to dserver

# %%
import dtool_lookup_api.asynchronous as dl

# %% [markdown]
# To test the connection with the remote dserver instance, we inspect the versions of all server-side plugins:

# %%
await dl.get_versions()

# %%
await dl.get_config()

# %% [markdown]
# List all registered base URIs.

# %%
await dl.get_base_uris()

# %% [markdown]
# Searches for the free text John in the base uri s3://test-bucket

# %%
await dl.get_datasets(free_text="John", base_uris=['s3://test-bucket'])

# %%
pagination = {}

# %% [markdown]
# Searches for the datasets with the tag core-family in the s3://test-bucket

# %%
await dl.get_datasets(base_uris=['s3://test-bucket'], tags=["core-family"], pagination=pagination, page_size=5)

# %% [markdown]
# Pagination gives the information regarding the current page number and the total number of pages 

# %%
pagination

# %%
await dl.get_datasets(base_uris=['s3://test-bucket'], tags=["core-family"], pagination=pagination, page_size=5, page_number=2)

# %% [markdown]
# Fetches a dataset with a particular uuid form the s3://test-bucket 

# %%
await dl.get_dataset('s3://test-bucket/e2d97c0c-390c-4e72-9905-316154cfc994')

# %% [markdown]
# # Searching using Mongo queries 

# %% [markdown]
# Getting the datasets from the mongo query 

# %%
await dl.get_datasets_by_mongo_query(query={},base_uris=['s3://test-bucket'])

# %% [markdown]
# Searching for a single tag using mongo query

# %%
await dl.get_datasets_by_mongo_query(query={"tags":"core-family"})

# %% [markdown]
# Searching multiple tags using mongo query 

# %%
await dl.get_datasets_by_mongo_query(query={"tags":["core-family","second-generation"]})

# %% [markdown]
# Searching for annotations using mongo query 

# %%
await dl.get_datasets_by_mongo_query(query={"annotations.Sex":"Male"})

# %% [markdown]
# Searching for tags and annotations using mongo query

# %%
await dl.get_datasets_by_mongo_query(query={"annotations.Sex":"Female", "tags": "core-family"})

# %% [markdown]
# Searching for the occurence of a keyword in the contact addresses using mongo query

# %%
await dl.get_datasets_by_mongo_query(query={"readme.contact.address":{"$regex": "Chicago"}})

# %% [markdown]
# ## Getting the annotations of a dataset by uri

# %%
await dl.get_annotations('s3://test-bucket/31b778e2-d2e6-4d5a-bba1-5580717b3bff')

# %% [markdown]
# ## Getting the tags of a dataset by uri

# %%
await dl.get_tags('s3://test-bucket/31b778e2-d2e6-4d5a-bba1-5580717b3bff')

# %% [markdown]
# ## Getting the manifest of a dataset by uri

# %%
await dl.get_manifest('s3://test-bucket/31b778e2-d2e6-4d5a-bba1-5580717b3bff')

# %% [markdown]
# ## Getting the readme of a dataset by uri

# %%
await dl.get_readme('s3://test-bucket/31b778e2-d2e6-4d5a-bba1-5580717b3bff')

# %% [markdown]
# ## Getting the graph of a particular dataset using the uuid

# %%
data = await dl.get_graph_by_uuid('31b778e2-d2e6-4d5a-bba1-5580717b3bff')

# %%
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

# %%
# Create a directed graph
G = nx.DiGraph()

# Adding nodes with labels
for item in data:
    name = item['name']
    tags = ', '.join(item.get('tags', []))
    label = f"{name}\n({tags})"
    G.add_node(item['uuid'], label=label)

# Adding edges from 'derived_from'
for item in data:
    child = item['uuid']
    for parent in item['derived_from']:
        G.add_edge(parent, child)

# %%
# Draw the graph with pygraphviz layout
plt.figure(figsize=(12, 8))
pos = graphviz_layout(G, prog='dot')  # Tree layout

node_labels = nx.get_node_attributes(G, 'label')
nx.draw(G, pos, with_labels=False, node_size=2500, node_color='lightblue', arrows=True)
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)

plt.title("Family Relationship Graph")
plt.axis('off')
plt.show()

# %% [markdown]
# ## Query provenance graph from dserver

# %% [markdown]
# Illustrates use of https://dtool-lookup-api.readthedocs.io/en/latest/generated/dtool_lookup_api.core.LookupClient.html#dtool_lookup_api.core.LookupClient.TokenBasedLookupClient.get_graph_by_uuid

# %% [markdown]
# ## Embed dtool in automated tasks

# %% [markdown]
# ## Appendix

# %%
import sys, os, errno
import logging
from shutil import copyfile

# %%
from dtoolcore import DataSet, ProtoDataSet, DataSetCreator, storagebroker, copy

# %%
with DataSetCreator("test-dataset", "/tmp", "TEST CONTENT") as ds_creator:
    animal_ds_uri = ds_creator.uri
    for animal in ["cat", "dog", "parrot"]:
        handle = animal + ".txt"  # Unix-like relpath
        fpath = ds_creator.prepare_staging_abspath_promise(handle)
        with open(fpath, "w") as fh:
            fh.write(animal)


# %%
# DataSetCreator?

# %%
def get_key(dataset):
    manifest = dataset.generate_manifest()
    return next(iter(manifest['items'].items()))[0]
    


# %%
dataset = DataSet.from_uri("/tmp/test-dataset")
first_key = get_key(dataset)
item_abspath = dataset.item_content_abspath(first_key)

# %%
another_dataset = DataSet.from_uri("s3://test-bucket/1a1f9fad-8589-413e-9602-5bbd66bfe675")
manifest2 = dataset.generate_manifest()
manifest2['items'].items()
#item_abspath2 = dataset.item_content_abspath(get_key(another_dataset))
another_dataset.
dtoolcore.copy("tmp/test-dataset2","s3://test-bucket/1a1f9fad-8589-413e-9602-5bbd66bfe675")

# %%
storagebroker.from_uri("s3://test-bucket/1a1f9fad-8589-413e-9602-5bbd66bfe675")

# %%
dataset2 = DataSet.from_uri("/tmp/test-dataset")
manifest = dataset.generate_manifest()
next(iter(manifest['items'].items()))[0]
manifest

# %%
copy("tmp/test-dataset","s3://test-bucket/1a1f9fad-8589-413e-9602-5bbd66bfe675")

# %%
protos = ProtoDataSet.create
protos.put_item("this")

# %%
