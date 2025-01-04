import http.server
import socketserver

PORT = 8000  # Specify the port you want to use
DIRECTORY = "./"  # Specify the directory you want to serve files from

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Open your web browser and go to http://localhost:{PORT}/")
    httpd.serve_forever()
