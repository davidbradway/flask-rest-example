# Python Flask RESTful API Example

## Using Virtualenv

    virtualenv my_flask_env
    source my_flask_env/bin/activate
    pip install -r requirements.txt
    set FLASK_APP=main.py
    flask run
    #http://localhost:5000/api/hello/david
    #http://localhost:5000/api/data
    # Test http://localhost:5000/api/add via PUT request using Postman Chrome App with json data {'a':1, 'b':2}
    py.test -v
    deactivate

## Using Conda

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
