# create fresh virtual environment
python -m venv venv
source venv/bin/activate

pip install wheel
pip install -r requirements.txt

dtool --help
dtool --version
