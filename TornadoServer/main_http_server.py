import sys, getopt
import tornado.ioloop
import tornado.web
import json
import model_one 

class MainHandler(tornado.web.RequestHandler):
    
    def initialize(self, model):
        self.__model= model

    def get(self):                       
        input_array = self.__get_input_array()
        result = self.__model.predict(input_array)
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

def make_app(config_file): 
    model = model_one.create_model_one(config_file)
    url_ext = r"/predict"
    return tornado.web.Application([
        (url_ext, MainHandler, dict(model=model)),
    ])


def get_args(argv):
    port=''
    config_file=''
    portAsInt=0    
    try:
        opts, args = getopt.getopt(argv,"hp:c:",["port=", "--config-file"])
    except getopt.GetoptError:
        sys_exit('', 1)        
    for opt, arg in opts:
        if opt == '-h':
            sys_exit('', 0)            
        elif opt in ("-p", "--port"):
            port = arg            
        elif opt in ("-c", "--config-file"):
            config_file= arg

    if port=='':
        sys_exit("must indicate port number", 2)        
    if( config_file==''):
        sys_exit("must indicate config file", 3)    
    try:
        portAsInt = int(port)
    except :
        sys_exit('invalid port number {}'.format(port),4)        
    return {'port':portAsInt, 'config_file':config_file}    

def sys_exit(message='', exit_code=0):    
    if message!='':
        print(message)
    usage = 'main_http_server.py -p <port> -c <config-file>'        
    print(usage)
    sys.exit(exit_code)


def main(argv):
    app_args = get_args(argv)
    print('config-file:{config_file}. port:{port}'.format( config_file=app_args["config_file"], port=app_args["port"]))
    app = make_app(app_args["config_file"])
    app.listen( app_args["port"] )
    print ('listening...')
    tornado.ioloop.IOLoop.current().start()   

if __name__ == "__main__":
    main(sys.argv[1:])