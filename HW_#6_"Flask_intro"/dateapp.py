from flask import Flask
from datetime import datetime, timedelta, timezone

app = Flask(__name__)


@app.route('/datetime')
def datetime_doc():
    app.logger.info('Showing manual documentation.')
    return '''Usage:
    - /datetime: returns brief documentation and an example
    - /datetime/: returns the current date and time in the server's time zone
    - /datetime/: returns the current date and time in the specified time zone
    Example:
    - /datetime: curl http://localhost:5000/datetime
    - /datetime/: curl http://localhost:5000/datetime/
    - /datetime/2: curl http://localhost:5000/datetime/2'''


@app.route('/datetime/')
@app.route('/datetime/<int:timezone_offset>')
def get_current_time(timezone_offset=3):
    app.logger.info('Shows timezone from manual int input, if blank shows actual time in Ukraine')
    try:
        tz = timezone(timedelta(hours=timezone_offset))
    except ValueError:
        return "Time zone not found", 406
    server_time = datetime.now(tz)
    return f"The current time is: {server_time}"


if __name__ == '__main__':
    # We need to set logging to be able to see everything
    import logging

    app.logger.setLevel(logging.DEBUG)

    # (!) Never run your app on '0.0.0.0 unless you're deploying
    #     to production, in which case a proper WSGI application
    #     server and a reverse-proxy is needed
    #     0.0.0.0 means "run on all interfaces" -- insecure
    app.run(host='127.0.0.1', port=5000, debug=True)
