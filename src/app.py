import http.server
import socketserver
import argparse
from urllib.parse import urlparse
from urllib.parse import parse_qs


PORT = 8080
class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        parsed_path = urlparse(self.path)
        query_components = parse_qs(parsed_path.query)
        message = '<html><body>'
        message += '<h1>Hi there!</h1>'
        message += '<p>You asked for <code>%s</code></p>' % self.path
        message += '<p>You asked for <code>%s</code></p>' % query_components
        message += '</body></html>'
        self.wfile.write(bytes(message, 'utf8'))
        return


#run the server to handle the get and post request and return the html page
def run_server(port):
    #create a server
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("Serving at port", port)
        #run the server
        httpd.serve_forever()


if __name__ == "__main__":
    #get the port from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=PORT, type=int, help="port to listen on")
    args = parser.parse_args()
    PORT = args.port

    #run the server
    run_server(PORT)