class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, l, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.l = l
        self.authors = authors
        self.astring = "Authors: "
        for i in self.authors:
            self.astring += f"\n- {i}"
        self.dstring = "Dependencies: "
        for i in self.dependencies:
            self.dstring += f"\n- {i}"
        self.devdstring = "Development dependencies: "
        for i in self.dev_dependencies:
            self.devdstring += f"\n- {i}"

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.l}\n"
            f"\n{self.astring}\n"
            f"\n{self.dstring}\n"
            f"\n{self.devdstring}"
        )
