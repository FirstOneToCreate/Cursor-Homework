def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    res = 'Hello WSGI world!'.encode('utf-8')
    return [res]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('127.0.0.1', 5000, app)
    try:
        print('Serving app...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    print('Server stopped')