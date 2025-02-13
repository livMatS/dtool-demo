# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
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

# %%
import dtoolcore

# %% [markdown]
# ## Create local dataset

# %% [markdown]
# ## Copy dataset to remote storage backend

# %% [markdown]
# ## Search and query entries on dserver

# %% [markdown]
# See documentation of dtool-lookup-api at https://dtool-lookup-api.readthedocs.io for a thorough documentation of posing queries to dserver

# %%
import dtool_lookup_api

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
