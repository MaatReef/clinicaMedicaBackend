from app import app
from livereload import Server # Hot reload

if __name__ == "__main__":
    server = Server(app.run(host="0.0.0.0", port=5000, debug=True, threaded=True))
    server.serve()                   # En Config seteamos lo necesario
