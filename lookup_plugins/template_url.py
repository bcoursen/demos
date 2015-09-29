## usage lookup('template_url', 'https://myserver/template.j2')
import urllib2
import tempfile
import os

from ansible import utils
from ansible.module_utils.urls import open_url, ConnectionError, SSLValidationError
from ansible.utils.unicode import to_unicode
from glob import glob

class LookupModule(object):
    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, inject=None, **kwargs):

        if isinstance(terms, basestring):
            terms = [ terms ]

        validate_certs = kwargs.get('validate_certs', True)
        f_handle, templ_path = tempfile.mkstemp(prefix='ansible_template', dir='/tmp/')
        temp_file = open(templ_path, 'w+r')
        ret = []
        for term in terms:
            try:
                response = open_url(term, validate_certs=validate_certs)
            except urllib2.URLError as e:
                utils.warnings("Failed lookup url for %s : %s" % (term, str(e)))
            except urllib2.HTTPError as e:
                utils.warnings("Received HTTP error for %s : %s" % (term, str(e)))
            except SSLValidationError as e:
                utils.warnings("Error validating the server's certificate for %s: %s" % (term, str(e)))
            except ConnectionError as e:
                raise utils.warnings("Error connecting to %s: %s" % (term, str(e)))
 
            for line in response.read().splitlines():
                temp_file.write(line)
            ret.append(templ_path)
        return ret
