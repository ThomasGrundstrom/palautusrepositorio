from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        d = toml.loads(content)
        dependencies = []
        dev_dependencies = []
        for i in d["tool"]["poetry"]["dependencies"]:
            dependencies.append(i)
        for i in d["tool"]["poetry"]["group"]["dev"]["dependencies"]:
            dev_dependencies.append(i)
        name = d["tool"]["poetry"]["name"]
        description = d["tool"]["poetry"]["description"]
        l = d["tool"]["poetry"]["license"]
        authors = d["tool"]["poetry"]["authors"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, l, authors)
