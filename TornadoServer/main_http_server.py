import tornado.ioloop
import tornado.web
import model_one 

class MainHandler(tornado.web.RequestHandler):

    
    def initialize(self, model_path):
        print("initialize")
        if not hasattr(self, "model"):
                    self.model = model_one.create_model_one(model_path)

    def get(self):
        result = self.model.predict([1,2,3,4,5,6,7,8])
        self.write( str(result[0][0]))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler, dict(model_path="gmm0.9.hdf5")),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()