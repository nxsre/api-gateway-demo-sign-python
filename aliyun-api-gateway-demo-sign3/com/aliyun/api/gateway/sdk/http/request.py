from com.aliyun.api.gateway.sdk.common import constant


class Request:
    content_md5 = "Content-MD5"
    content_length = "Content-Length"
    content_type = "Content-Type"

    def __init__(self, host=None, port=None, protocol=constant.HTTP, headers=None, url=None, method=None, time_out=None):
        if headers is None:
            headers = {}
        self.__host = host
        self.__port = port
        self.__url = url
        self.__method = method
        self.__time_out = time_out
        self.__headers = headers
        self.__body = None
        self.__content_type = None
        self.__query_str = None
        self.__protocol = protocol
        self.__key_file = None
        self.__cert_file = None

    def get_protocol(self):
        return self.__protocol

    def set_protocol(self, protocol):
        self.__protocol = protocol

    def get_method(self):
        return self.__method

    def set_method(self, method):
        self.__method = method

    def get_host(self):
        return self.__host

    def get_port(self):
        return self.__port

    def set_host(self, host):
        self.__host = host

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def get_time_out(self):
        return self.__time_out

    def set_time_out(self, time_out):
        self.__time_out = time_out

    def get_content_type(self):
        return self.__content_type

    def set_content_type(self, content_type):
        self.__content_type = content_type

    def get_headers(self):
        return self.__headers

    def set_headers(self, headers=None):
        if headers is None:
            headers = {}
        self.__headers = headers

    def get_query_str(self):
        return self.__query_str

    def set_query_str(self, query_str=None):
        self.__query_str = query_str

    def set_body(self, body):
        self.__body = body

    def get_body(self):
        return self.__body

    def set_key_file(self, key_file):
        self.__key_file = key_file

    def get_key_file(self):
        return self.__key_file

    def set_cert_file(self, cert_file):
        self.__cert_file = cert_file

    def get_cert_file(self):
        return self.__cert_file
