from flask import Flask
from datetime import datetime, timedelta, timezone

app = Flask(__name__)


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
