# -*- coding: utf-8 -*-
from tornado.httpclient import AsyncHTTPClient

AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')

AsyncClient = AsyncHTTPClient()