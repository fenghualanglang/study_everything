import redis


class RedisDB(object):
    def __init__(self, conf):
        self.conn = redis.Redis(
            connection_pool=redis.ConnectionPool(
                host=conf['redis_host'],
                port=conf['redis_port'],
                db=conf['redis_db'],
                password=conf['redis_passwd']
            )
        )

    def set(self, key, value, expire=None):
        self.conn.set(key, value, expire)

    def get(self, key):
        return self.conn.get(key)

    def setex(self, key, expire_time, strval):
        return self.conn.setex(key, expire_time, strval)

    def delete(self, key):
        self.conn.delete(key)

    def hdel(self, name, key):
        return self.conn.hdel(name, key)

    def hset(self, name, key, value):
        self.conn.hset(name, key, value)

    def hget(self, key, fields):
        return self.conn.hget(key, fields)

    def hmset(self, key, fields):
        self.conn.hmset(key, fields)

    def hgetall(self, name):
        data = self.conn.hgetall(name)
        data = dict((item[0].decode('utf-8'), item[1].decode('utf-8')) for item in data.items()) if data else None
        return data

    def hvals(self, key):
        return self.conn.hvals(key)

    def hkeys(self, key):
        return self.conn.hkeys(key)

    # def hdel(self, key, field):
    #     self.conn.hdel(key, field)

    def exists(self, key):
        return self.conn.exists(key)

    def hexists(self, name, key):
        return self.conn.hexists(name, key)

    # def delete(self, *names):
    #     return self.conn.delete(*names)

    def expire(self, name, time):
        return self.conn.expire(name, time)
