call conda env remove-n venv
call conda create -n venv python=3.8
call conda activate venv
call conda install -c conda-forge pythonocc-core=7.8.1
call conda install occt
pip install -r requirements-init.txt