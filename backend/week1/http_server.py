from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = 'localhost'
PORT = 8000

class myHTTP(BaseHTTPRequestHandler):
    def do_GET(self): #response to get request
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>My first page</title></head><body><h1>HELLO WORLD</h1></body>", "utf-8"))
        #eg. ML use, pass image to request, and write the result of classification here

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "%s"}' % date, "utf-8"))



server = HTTPServer((HOST, PORT), myHTTP)
print('Server running on port %s:%s ...' % (HOST, PORT))
server.serve_forever()
server.server_close()