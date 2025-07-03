import sys
sys.path.append("./backend")

from WebServer import WebServer

def main(args):
    if len(args) == 1:
        web = WebServer()
        if (args[0] == 'run'):
            web.run()
        elif args[0] == 'test':
            web.console_test()
        else:
            print ("python run.py run  --> run api")
            print ("python run.py test --> run console test")
    else:
        print ("python run.py run  --> run api")
        print ("python run.py test --> run console test")
            

if __name__ == '__main__':
    main(sys.argv[1:])