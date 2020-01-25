from pulumi import ResourceOptions
from pulumi.dynamic import Resource
from typing import Any, Optional
from .FileFormatProvider import FileFormatProvider

class FileFormat(Resource):
    def __init__(self, name: str, props: Any, opts: Optional[ResourceOptions] = None):
        super().__init__(FileFormatProvider(), name, props, opts)