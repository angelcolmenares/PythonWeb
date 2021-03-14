import sys, getopt
import tornado.ioloop
import tornado.web
import json
import model_one 

class MainHandler(tornado.web.RequestHandler):
    
    def initialize(self, model_path):
        if not self.__is_model_initialized():
            self.model = model_one.create_model_one(model_path)
            self.__set_model_as_initialized()

    def get(self):                       
        input_array = self.__get_input_array()
        result = self.model.predict(input_array)
        self.write({'prediction': str(result[0][0])})

    def __get_input_array(self):
        input_one  = float( self.get_argument("inputOne"))
        input_two = float( self.get_argument("inputTwo"))
        input_three = float( self.get_argument("inputThree"))
        input_four = float( self.get_argument("inputFour"))
        input_five = float( self.get_argument("inputFive"))
        input_six = float( self.get_argument("inputSix"))
        input_seven = float( self.get_argument("inputSeven"))
        input_eigth = float( self.get_argument("inputEigth"))
        return [input_one,input_two, input_three, input_four,input_five,input_six,input_seven,input_eigth]

    def __is_model_initialized(self):
        return  hasattr(self, "__model_initialized__") and self.__model_initialized__
    
    def __set_model_as_initialized(self):
        self.__model_initialized__= True


def make_app():    
    url_ext = r"/predict" 
    return tornado.web.Application([
        (url_ext, MainHandler, dict(model_path="gmm0.9.hdf5")),
    ])


def main(argv):
    port=''
    try:
        opts, args = getopt.getopt(argv,"hp:",["port="])
    except getopt.GetoptError:
        print('main_http_server.py -p <port>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print( 'main_http_server.py -p <port>')
            sys.exit()
        elif opt in ("-p", "--port"):
            port = arg
            
    if port=='':
        print('main_http_server.py -p <port>')
        sys.exit(2)             
      
    print ('listen on port ', int(port))

    app = make_app()
    app.listen( int(port))
    print ('listening...')
    tornado.ioloop.IOLoop.current().start()   

if __name__ == "__main__":
    main(sys.argv[1:])