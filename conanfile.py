from conans import ConanFile
from conans.tools import load
import re


def get_version():
    try:
        content = load("src/CMakeLists.txt")
        version = re.search(b"set\(MY_LIBRARY_VERSION (.*)\)", content).group(1)
        return version.strip()
    except Exception as e:
        return None

class HelloConan(ConanFile):
    name = "Hello"
    version = get_version()
    
    def source(self):
        self.output.info("SOURCE: %s" % self.version)

    def build(self):
        self.output.info("BUILD: %s" % self.version)

    def package(self):
         self.output.info("PACKAGE: %s" % self.version)

    def package_info(self):
         self.output.info("PACKAGE_INFO: %s" % self.version)
