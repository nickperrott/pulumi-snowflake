from pulumi.dynamic import ResourceProvider, CreateResult

class FileFormatProvider(ResourceProvider):
    def create(self, inputs):
        return CreateResult(id_="foo", outs={})
