import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

# 创建application对象, 对服务器进行若干设置, 包括路由列表等
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello tornado')


app = Application([('/', IndexHandler)])

#创建服务端server程序

server =HTTPServer(app)

#服务端监听段端口
server.listen(8888)

#启动服务程序 在当前进程中启动服务
IOLoop.current().start()





