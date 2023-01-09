from jinja2 import Template
import os
from .template.pom_xml import POM_TEMPLATE_CONTENT
from .template.application_yaml import APPLICATION_YAML_TEMPLATE
from .template.index_html import INDEX_HTML_TEMPLATE
from .template.security_constraint import SECURITY_BINDING_YAML_TEMPLATE

class IndyService(object):
    """This IndyService will represent a simple model data content which will be
    used in rendering service related files, like pom.xml and application.yaml
    """
    def __init__(self, project_dir: str, artifact_id: str, name=None,
                 desc=None, repo_name=None, enable_security=True,
                 enable_event=True, enable_tracing=True):
        self.group_id="org.commonjava.indy.service"
        self.project_dir = project_dir
        self.artifact_id = artifact_id
        self.name = name
        if not self.name:
            self.name = self.artifact_id
        self.desc = desc
        if not self.desc:
            self.desc = self.artifact_id
        self.repo_name = repo_name
        if not self.repo_name:
            self.repo_name = self.artifact_id
        self.enable_security=enable_security
        self.enable_event=enable_event
        self.enable_tracing=enable_tracing
        
    def render_pom(self) -> str:
        template = Template(POM_TEMPLATE_CONTENT)
        return template.render(service=self)
    
    def render_appconf(self) -> str:
        template = Template(APPLICATION_YAML_TEMPLATE)
        return template.render(service=self)
    
    def render_index_html(self) -> str:
        template = Template(INDEX_HTML_TEMPLATE)
        return template.render(service=self)
    
    def render_sec_constraint(self) -> str:
        template = Template(SECURITY_BINDING_YAML_TEMPLATE)
        return template.render(service=self)
    
    def gen_project(self):
        base_dir = os.path.join(self.project_dir, self.artifact_id)
        _write_to_file(base_dir, self.render_pom(), "pom.xml")
        _make_java_directories(base_dir, pkgs=self.group_id.split("."))
        res_dir = os.path.join(base_dir, "src/main/resources")
        _write_to_file(res_dir, self.render_appconf(), "application.yaml")
        if self.enable_security:
            _write_to_file(res_dir, self.render_sec_constraint(), "security-bindings.yaml")
        meta_inf_res_dir = os.path.join(res_dir, "META-INF", "resources")
        _write_to_file(meta_inf_res_dir, self.render_index_html(), "index.html")
        
        
def _write_to_file(base_dir:str, content:str, file_name:str):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    file = os.path.join(base_dir, file_name)
    with open(file, mode="w", encoding="utf-8") as f:
        f.write(content)
    print("{file} created successfully.".format(file=file))

def _make_java_directories(base_dir: str, pkgs=None):
    src_dir = os.path.join(base_dir, "src/main/java")
    if not os.path.exists(src_dir):
        os.makedirs(src_dir)
    res_dir = os.path.join(base_dir, "src/main/resources")
    if not os.path.exists(res_dir):
        os.makedirs(res_dir)
    test_src_dir = os.path.join(base_dir, "src/test/java")
    if not os.path.exists(test_src_dir):
        os.makedirs(test_src_dir)
    test_res_dir = os.path.join(base_dir, "src/test/resources")
    if not os.path.exists(test_res_dir):
        os.makedirs(test_res_dir)
    if pkgs:
        src_pkg_dirs = os.path.join(src_dir, *pkgs)
        if not os.path.exists(src_pkg_dirs):
            os.makedirs(src_pkg_dirs)
        test_src_pkg_dirs = os.path.join(test_src_dir, *pkgs)
        if not os.path.exists(test_src_pkg_dirs):
            os.makedirs(test_src_pkg_dirs)
        
        