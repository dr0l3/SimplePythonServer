from http.server import BaseHTTPRequestHandler, HTTPServer


class TestHTTPServerRequestHandler(BaseHTTPRequestHandler):
    def do_get(self):
        self.send_response(200)

        self.send_header('content-type', 'text/html')
        self.end_headers()

        message = "hello world"

        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    print("starting server...")

    server_address = ("127.0.0.1", 8081)
    httpd = HTTPServer(server_address, TestHTTPServerRequestHandler)
    print("running server...")
    httpd.serve_forever()


run()
