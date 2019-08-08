import sys
from pywren_ibm_cloud.utils import version_str

IBM_AUTH_ENDPOINT_DEFAULT = 'https://iam.cloud.ibm.com/oidc/token'

RUNTIME_DEFAULT_35 = 'ibmfunctions/pywren:3.5'
RUNTIME_DEFAULT_36 = 'ibmfunctions/action-python-v3.6'
RUNTIME_DEFAULT_37 = 'ibmfunctions/action-python-v3.7'

RUNTIME_TIMEOUT_DEFAULT = 600000  # Default: 600000 milliseconds => 10 minutes
RUNTIME_MEMORY_DEFAULT = 256  # Default memory: 256 MB


def load_config(config_data=None):
    if 'runtime_memory' not in config_data['pywren']:
        config_data['pywren']['runtime_memory'] = RUNTIME_MEMORY_DEFAULT
    if 'runtime_timeout' not in config_data['pywren']:
        config_data['pywren']['runtime_timeout'] = RUNTIME_TIMEOUT_DEFAULT
