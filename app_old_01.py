import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    '''
    リクエストハンドラクラス
    '''
    def get(self):
        '''
        GETリクエストの対応
        '''
        self.write("Hello, world")

application = tornado.web.Application([
    '''
    アプリケーション全体の設定をする
    '''

    # ルートへアクセスがあった場合
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
