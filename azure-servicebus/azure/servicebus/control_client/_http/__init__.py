﻿# ------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------

 # pylint: disable=too-few-public-methods


class HTTPError(Exception):

    ''' HTTP Exception when response status code >= 300 '''

    def __init__(self, status, message, respheader, respbody):
        '''Creates a new HTTPError with the specified status, message,
        response headers and body'''
        self.status = status
        self.respheader = respheader
        self.respbody = respbody
        Exception.__init__(self, message)


class HTTPResponse(object):

    """Represents a response from an HTTP request.  An HTTPResponse has the
    following attributes:

    status:
        the status code of the response
    message:
        the message
    headers:
        the returned headers, as a list of (name, value) pairs
    body:
        the body of the response
    """

    def __init__(self, status, message, headers, body):
        self.status = status
        self.message = message
        self.headers = headers
        self.body = body


class HTTPRequest(object):

    '''Represents an HTTP Request.  An HTTP Request consists of the following
    attributes:
    host:
        the host name to connect to
    method:
        the method to use to connect (string such as GET, POST, PUT, etc.)
    path:
        the uri fragment
    query:
        query parameters specified as a list of (name, value) pairs
    headers:
        header values specified as (name, value) pairs
    body:
        the body of the request.
    protocol_override:
        specify to use this protocol instead of the global one stored in
        _HTTPClient.
    '''

    def __init__(self):
        self.host = ''
        self.method = ''
        self.path = ''
        self.query = []      # list of (name, value)
        self.headers = []    # list of (header name, header value)
        self.body = ''
        self.protocol_override = None
