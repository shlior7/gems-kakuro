python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
virtualenv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
pip install --upgrade setuptools
python3 setup.py build
python3 setup.py install
