from jinja2 import Template
import os
import logging
from .template import POM_TEMPLATE_CONTENT, APPLICATION_YAML_TEMPLATE

logger = logging.getLogger("indy_serv_gen")

class IndyService(object):
    """This IndyService will represent a simple model data content which will be
    used in rendering service related files, like pom.xml and application.yaml
    """
    def __init__(self, artifact_id: str, name=None,
                 desc=None, repo_name=None, enable_security=True,
                 enable_event=True, enable_tracing=True):
        self.artifact_id = artifact_id
        self.name = name
        if not self.name:
            self.name = self.artifact_id
        self.desc = desc
        if not self.desc:
            self.desc = self.artifact_id
        self.repo_name = repo_name
        self.enable_security=enable_security
        self.enable_event=enable_event
        self.enable_tracing=enable_tracing
        
    def render_pom(self) -> str:
        template = Template(POM_TEMPLATE_CONTENT)
        return template.render(service=self)
    
    def render_appconf(self) -> str:
        template = Template(APPLICATION_YAML_TEMPLATE)
        return template.render(service=self)
