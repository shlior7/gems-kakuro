python3 -m ensurepip --upgrade
if [ -n "$PYTHON" ]; then
  python -m pip install --user virtualenv
  virtualenv -p python${PYTHON:0:1} venv
  source venv/bin/activate
elif [ -n "$CONDA" ]; then
  wget -O miniconda.sh https://repo.continuum.io/miniconda/Miniconda${CONDA:0:1}-latest-Linux-x86_64.sh
  bash miniconda.sh -b -p $HOME/miniconda
  export PATH="$HOME/miniconda/bin:$PATH"
  conda config --set always_yes yes --set changeps1 no
  conda config --add channels conda-forge
  conda update -q conda
  conda install -q conda-build
  conda create -q -n test-environment python=$CONDA
  source activate test-environment
fi

if [ -n "$PYTHON" ]; then
  python -m pip install .
elif [ -n "$CONDA" ]; then
  conda build conda.recipe --python $CONDA
  conda install --use-local kakuro
fi


python3 -m pip install . -vvv
