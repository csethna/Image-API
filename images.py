import json
import falcon

class Resource(object): # just a regular class
    def on_get(self, req, resp): # function defines HTTP resource // on_* where * is any standard HTTP method, lowercase
        doc = {
            'images': [
                {
                'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        # Create JSON representation ofo the Resource
        resp.body = json.dumps(doc, ensure_ascii=False)

        resp.status = falcon.HTTP_200 # 200 is the default response but can be overridden as-needed
