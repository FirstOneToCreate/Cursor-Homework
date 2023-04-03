from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def basic():
    app.logger.info('Reached hello route')
    return '<h1>Hello, Flask!</h1>'


# request parameters (aka in-route)
@app.route('/hello/<name>.<int:age>')
def hello(name, age):
    app.logger.info('Name is %r, age is %s', name, age)

    return f'Hello, {name}!\nYou are {age} years old.'


# parameter defaults
#   this 1st passes no args, so python defaults are used
@app.route('/hi/')         
@app.route('/hi/<name>')
def hi(name='Flask'):
    app.logger.info('Name is %r', name)

    return f'Hello, {name}!'


# parameter defaults
#   this passes defaults using Werkzeug route implementation
# Also require a name to be starting from capital letter
@app.route('/greet/', defaults={'name': 'Flask'})      
@app.route('/greet/<name>')
def greet(name):
    app.logger.info('Name is %r', name)

    if name[0].islower():
        abort(406, 'Name must start with a capital letter')

    return f'Hello, {name}!'


# parameter defaults using routes       (!) this one is decoupled
#   usually this way is used to return API descriptions
@app.route('/greet')     
def greet_def():
    return 'DEFROUTE (placeholder for api descr)'


@app.route('/noparam/')      # change to '/noparam' and see the difference
def noparam():
    return 'route without params'


if __name__ == '__main__':
    # We need to set logging to be able to see everything
    import logging
    app.logger.setLevel(logging.DEBUG)

    # (!) Never run your app on '0.0.0.0 unless you're deploying
    #     to production, in which case a proper WSGI application
    #     server and a reverse-proxy is needed
    #     0.0.0.0 means "run on all interfaces" -- insecure
    app.run(host='127.0.0.1', port=5000, debug=True)
