import os
import tempfile
from base64 import b64decode
from collections import namedtuple

CredentialPlugin = namedtuple('CredentialPlugin', ['name', 'inputs', 'backend'])

class CredGlobFiles:
    def __init__(self, glob):
        self.glob = glob
    
    def __enter__(self):
        if not self.glob:
            return None
        self.globfile = tempfile.NamedTemporaryFile('wb', delete=False)
        self.globfile.write(self.glob.encode())
        self.globfile.flush()
        return str(self.globfile.name)

    def __exit__(self):
        if self.globfile and os.path.exists(self.globfile.name):
            os.remove(self.globfile.name)

_inputs = {
    'fields': [{
        'id': 'secret',
        'label': 'Secret Base64 Variable',
        'type': 'string',
        'secret': True,
    }],
    'required': ['secret'],
}


def _backend(**kwargs):
    path = kwargs.get('url')
    secret = kwargs.get('secret')

    data = b64decode(secret)

    globfile = CredGlobFiles(data)
    globfile.__enter__()

    os.environ['JKS_INJECT_FILE'] = str(globfile.name)

    # backend_return = {
    #     JKS_INJECT_FILE = str(globfile.name)
    # }
    return os.environ['JKS_INJECT_FILE']

b64tofile_plugin = CredentialPlugin('Base64 String to File Credential Plugin', inputs=_inputs, backend=_backend)
