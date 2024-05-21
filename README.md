[![DOI:10.5281/zenodo.11237941](https://zenodo.org/badge/DOI/10.5281/zenodo.11237942.svg)](https://zenodo.org/doi/10.5281/zenodo.11237941)

# dtool-demo

A few simple samples on how to use [dtool](https://dtool.readthedocs.io/en/latest/) on the command line.

* [Setup](005-setup/README.md)
* [Copy from remote](008-copy-from-remote/README.md)
* [Dataset creation](010-dataset-creation/README.md)
* [Copy to remote](015-copy-to-remote/README.md)
* [Search and query](018-search-and-query/README.md)

# Recordings

Created with `asciinema`, stdin held within `stdin_file`, `xdotool`, `terminator` and `play_stdin.sh` replay script.

Expects `asciinema` installed within `venv` of repository root.

Uses `asciinema` config file as found below `asciinema` here.

Uses

```bash
# set default asciinema prompt
if [ -n "${ASCIINEMA_REC}" ]; then
  export PS1='> '
fi
```

entry within `.bashrc` for simple '> ' prompt in recording.

Requires `terminator`

See `scripts` folder for more information on how to reproduce recordings.

# Mock datasets

The `scripts` folder holds snippets for the generation of several hundred mock datasets.
These datasets are filled with metadata from `README.yml` files within `sample-content`.
