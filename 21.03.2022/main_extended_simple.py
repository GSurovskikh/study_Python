from http.server import HTTPServer, SimpleHTTPRequestHandler


PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):

    def __init__(self,*args,**kwargs):
        super(MyHandler, self).__init__(*args,**kwargs)

    def do_GET(self):
        if self.path == "/test":
            self.path = "page2.html"
        super().do_GET()

    def do_POST(self):
        super.do_POST()

if __name__ == '__main__':
    try:
        with HTTPServer(("localhost",PORT),MyHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        pass