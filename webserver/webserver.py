import http.server
import socketserver
import os

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Define paths and corresponding HTML files
        routes = {
            "/": "index.html",
        }

        # Get the requested path
        requested_path = self.path

        # Get the file to serve based on the path
        file_to_serve = routes.get(requested_path, None)

        if file_to_serve:
            # Serve the corresponding HTML file if it exists
            if os.path.exists(file_to_serve):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                with open(file_to_serve, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                # If the file doesn't exist, serve a 404 error
                self.send_error(404, "File not found")
        else:
            # If the path is not in the routes, serve a 404 error
            self.send_error(404, "File not found")

def run():
    port = 8080

    # Create the custom handler_class (a handler is a block of code that gets triggered when a certain event or request happens)
    handler=CustomHandler

    # set the server address with the port number
    server_address = ('', port)

    # Create the http process
    httpd = socketserver.TCPServer(server_address, handler)

    # Tell the user which port the server is running on
    print(f'Server running on port {port}. Go to http://localhost:{port}')

    # Run the server until manually stopped
    httpd.serve_forever()

if __name__ == "__main__":
    run()