python3 -m ensurepip --upgrade
python3 -m pip install virtualenv
virtualenv .venv
source .venv/bin/activate
python3 -m pip install . -vvv
ls -A
cd .venv/lib
ls
