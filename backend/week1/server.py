from http.server import HTTPServer, BaseHTTPRequestHandler

url_map = {}

class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        requested_path = self.path
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Custom-header', 'hello customizer')
        self.end_headers()

        response_content = "Hello, demo response content" + self.path

        self.wfile.write(response_content.encode('utf-8'))

class URLShortener(BaseHTTPRequestHandler):
    def do_GET(self):
        path_split = self.path.split('/')
        shortcode = path_split[2]

        if shortcode in url_map:
            self.send_response(302)
            self.send_header('Location', url_map[shortcode])
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            request_content = f"While its true that shortcode {shortcode} is not found, heres: HELLO WORLD!"
            self.wfile.write(request_content.encode('utf-8'))

    def do_POST(self):
        path_split = self.path.split('/')
        shortcode = path_split[2]
        dest = '/'.join(path_split[3:])

        self.send_response(201)
        self.end_headers()

        url_map[shortcode] = dest

if __name__ == '__main__':
    addr = ('localhost', 8000)
    server = HTTPServer(addr, URLShortener)
    print('Server running on port %s:%s ...' % ('localhost', 8000))
    
    #Start the server
    server.serve_forever()
    server.server_close()