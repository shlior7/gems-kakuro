python3 -m pip install virtualenv
virtualenv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 setup.py install
python3 -m pip install . -vvv
python setup.py build
python setup.py install
python -m pip install . -vvv
