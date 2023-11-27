import os

import cherrypy
from cherrypy.process.plugins import PIDFile


class Root:
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self) -> str:
        result = {"operation": "request", "result": "success"}
        return result

def run():
    cur_dir = os.path.abspath(os.path.dirname(__file__))

    cherrypy.config.update({
        "environment": "production",
        "log.screen": True,
        "server.socket_port": 8444,
        "server.ssl_module": "builtin",
        "server.ssl_private_key": os.path.join(cur_dir, "key.pem"),
        "server.ssl_certificate": os.path.join(cur_dir, "cert.pem")
    })
    PIDFile(cherrypy.engine, 'bookmark.pid').subscribe()
    cherrypy.quickstart(Root())


if __name__ == '__main__':
    run()
