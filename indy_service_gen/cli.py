import logging
import locale
import sys
from .project import IndyService

logger = logging.getLogger("indy_serv_gen")

PROG="indy_service_gen"

class CLI(object):
    def __init__(self):
        locale.setlocale(locale.LC_ALL, "")
        
    def run(self):
        logging.captureWarnings(True)
        service_name=input("Please input your service name:")
        if not service_name:
            print("Service name can not be empty!")
            sys.exit(1)
            
        artifact_id = input("Input the service maven artifact id:")
        if not artifact_id:
            print("Service maven artifact_id can not be empty!")
            sys.exit(1)
        
        service_desc = input("Input the service description[{name}]:".format(name=service_name))
        if not service_desc:
            service_desc=service_name
            
        enable_security=True
        enable_sec = input("Enable security settings?[y]:")
        if enable_sec=="n" or enable_sec=="N":
            enable_security=False
        
        enable_event=True
        enable_evt = input("Enable kafka event settings?[y]:")
        if enable_evt=="n" or enable_evt=="N":
            enable_event=False
        
        enable_tracing=True
        enable_tra = input("Enable opentelemetry tracing settings?[y]:")
        if enable_tra=="n" or enable_tra=="N":
            enable_tracing=False
        
        service = IndyService(artifact_id=artifact_id, name=service_name,
                              desc=service_desc, enable_security=enable_security,
                              enable_event=enable_event, enable_tracing=enable_tracing)
        print(service.render_pom())
        print("\n\n\n")
        print(service.render_appconf())

        


def gen_project(args):
    '''TODO: implement this method'''
    pass

def run():
    cli = CLI()
    cli.run()

def exception_message(exc):
    """
    Take an exception and return an error message.
    The message includes the type of the exception.
    """
    return '{exc.__class__.__name__}: {exc}'.format(exc=exc)

if __name__ == "__main__":
    run()
