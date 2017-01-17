from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.wfile.write("hello world")
if __name__=="__main__":
	server =HTTPServer(("", 8888),MyHandler)
	print("started webserver on port 8888...")
	print("press ^C to shut the server")
	server.serve_forever()
