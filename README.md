# dtool-demo

A few simple samples on how to use dtool on the command line.

* [Setup](005-setup/README.md)
* [Copy from remote](008-copy-from-remote/README.md)
* [Dataset creation](010-dataset-creation/README.md)
* [Copy to remote](015-copy-to-remote/README.md)
* [Search and query](018-search-and-query/README.md)

# Recordings

Created with `asciinema`, stdin held within `stdin_file`, `xdotool`, `terminator` and `play_stdin.sh` replay script.

Expects `asciinema` installed within venv `${HOME}/venv/jlh-imtek-python-3.8/bin/activate`.

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
