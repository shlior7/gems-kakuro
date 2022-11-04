python3 -m pip install virtualenv
virtualenv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 setup.py install
