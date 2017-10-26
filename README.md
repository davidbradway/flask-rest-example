# Python Flask RESTful API Example

## Using Virtualenv

    virtualenv -p python3 my_flask_env
    source my_flask_env/bin/activate
    pip install -r requirements.txt
    # Windows:
    set FLASK_APP=main.py
    flask run
    # Linux:
    FLASK_APP=main.py flask run --host=0.0.0.0
    #http://localhost:5000/api/hello/david
    #http://localhost:5000/api/data
    # Test http://localhost:5000/api/add via PUT request using Postman Chrome App with json data {'a':1, 'b':2}
    py.test -v
    deactivate

## Using Conda

### Setup Miniconda

    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh # Fetch this file from the internet to your machine
    chmod +x Miniconda3-latest-Linux-x86_64.sh # Allow this file to be executable
    ./Miniconda3-latest-Linux-x86_64.sh # Execute this shell script
    source ~/.bashrc # Re-source bashrc to pull in latest config

### Setup Environment

    conda create -n my_flask_env
    activate my_flask_env
    pip install -r requirements.txt
    set FLASK_APP=main.py
    flask run
    #http://localhost:5000/api/hello/david
    #http://localhost:5000/api/data
    # Test http://localhost:5000/api/add via PUT request using Postman Chrome App with json data {'a':1, 'b':2}
    py.test -v
    deactivate
