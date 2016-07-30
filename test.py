from ete3_webserver import WebTreeHandler, start_server

class CustomHandler(WebTreeHandler):
    pass


start_server(CustomHandler)
