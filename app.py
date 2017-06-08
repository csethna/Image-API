import falcon

from .images import Resource

api = application = falcon.API() # Creates WSGI (web server gateway interface) application and aliases "api"
# Gunicorn, by default searches for "application"
#ipython REPL = read, evaluate, print, loop
images = Resource()
# # when a request comes in for 'images', Falcon will call the responder on the images resource that correspondes to the requested HTTP method.
api.add_route('/images', images)
