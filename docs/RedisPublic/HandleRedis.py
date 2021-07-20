import redis

##需要将远程redis 的保护模式 设置为no 以及将bind ：127.0.0.1注释掉

class HandleRedis:
    def __init__(self, host, port, db, decode_responses, password):
        self.host = host
        self.port = port
        self.db = db
        self.decode_responses = True
        self.password = ''
        self.rdb = None

    def getConnect(self):
        try:
            pool =redis.ConnectionPool(host=self.host,port=self.port,db=self.db,decode_responses=self.decode_responses,password=self.password,socket_connect_timeout=1)
            self.rdb = redis.StrictRedis(connection_pool=pool)
            Flag = self.rdb.ping()
            if Flag:
                return self.rdb
        except Exception as e:
            return {"connection fails":e}


#
# if __name__ == '__main__':
#     HR = None
#     HR = HandleRedis(host="82.156.75.223", port=6379, db=0, decode_responses=True, password='')
#     conn =HR.getConnect()
#     print(conn)


