# Indy Service Project Generator

This tool is used to generate a skeleton of indy service maven project.

## Prerequisites

* python 3.5+
* git

## Installation

### From git

Clone this git repo and install charon using python installer:

```bash
git clone https://github.com/Commonjava/indy-service-gen.git
cd indy-service-gen
pip install --upgrade pip --user
pip install virtualenv --user
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements-dev.txt
python setup.py install 
```

## Command guide

* Basic command: indy_service_gen
* The prompt items as below:

  * Please input your service name: The name which will be used in maven pom.xml, like "Indy Repository Service"
  * Input the service maven artifact id: The artifactId which will be used in maven pom.xml. (e.g indy-repository-service)
  * Input the service description: The description which will be used in maven pom.xml, will be same with service name if not provided
  * Enable security settings?: Will add security relate dependencies and settings if enabled, default is yes
  * Enable kafka event settings?: Will add kafka related dependencies and settings if enabled, default is yes
  * Enable opentelemetry tracing settings?: Will add opentelemetry tracing dependencies and settings if enabled, default is yes
  * Input your directory where your project will be generated: Where you want to generate your project skeleton, If not provided will ask if current directory is ok
