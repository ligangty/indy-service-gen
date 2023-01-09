import locale
import sys
import os
from .project import IndyService

PROG="indy_service_gen"

class CLI(object):
    def __init__(self):
        locale.setlocale(locale.LC_ALL, "")
        
    def run(self):
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
            
        project_dir = _input_project_dir()
        while not os.path.exists(project_dir):
            print("The directory does not exist!")
            project_dir = _input_project_dir()
        
        service = IndyService(project_dir=project_dir, artifact_id=artifact_id,
                              name=service_name, desc=service_desc,
                              enable_security=enable_security, enable_event=enable_event,
                              enable_tracing=enable_tracing)
        
        service.gen_project()

def _input_project_dir() -> dir:
    project_dir = input("Input your directory where your project will be generated:")
    if not project_dir:
        gen_ok_in = input("The project directory is not provided, will use current directory[{dir}] as default, is it ok?[Y]:".format(dir=os.getcwd()))
        gen_ok_in = gen_ok_in.lower()
        if not gen_ok_in:
            gen_ok_in = "y"
        while gen_ok_in not in ["y", "n", "yes", "no"]:
            gen_ok_in = input("Input not correct. Please input yes or no (y or n) to continue:")
            gen_ok_in = gen_ok_in.lower()
        if gen_ok_in == "n":
            print("Generation not allowed. Exit now")
            sys.exit(0)
        project_dir = os.getcwd()
    
    return project_dir

def run():
    cli = CLI()
    cli.run()

if __name__ == "__main__":
    run()
