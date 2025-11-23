#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      Competición - ABDB                                ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        19/11/2025  -  05:00:00           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    23/11/2025  -  11:34:43           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================# 

import redis
import time

print("=== AEC3 tester ===")
r = redis.Redis(db=1, decode_responses=True)

def assert_eq(a, b, msg=""):
    if a != b:
        print(f"FAIL: {msg} ({a} != {b})")
    else:
        print("OK")

# Limpieza inicial
r.flushdb()

# Test 1: Reserva
r.hset("vehiculo:TEST001", mapping={"matricula":"TEST123","marca":"Mercedes","modelo":"Sprinter","tipo":"furgoneta","estado":"disponible","ubicacion":"Madrid Centro","precio_dia":89.50})
r.sadd("vehiculos:tipo:furgoneta", "TEST001")
r.zadd("ranking:vehiculos:popularidad", {"TEST001": 0})
r.set("stats:vehiculos:disponibles", 1)
r.set("stats:reservas:activas", 0)
pipe = r.pipeline()
pipe.hset("reserva:TEST_R001", mapping={"vehiculo_id":"TEST001","cliente_id":"TEST_C001","precio":89.50,"estado":"confirmada"})
pipe.expire("reserva:TEST_R001", 3600)
pipe.hset("vehiculo:TEST001", "estado", "en_uso")
pipe.decr("stats:vehiculos:disponibles")
pipe.incr("stats:reservas:activas")
pipe.zincrby("ranking:vehiculos:popularidad", 1, "TEST001")
pipe.execute()
assert_eq(r.hget("reserva:TEST_R001", "estado"), "confirmada")
assert_eq(int(r.get("stats:vehiculos:disponibles")), 0)
assert_eq(int(r.get("stats:reservas:activas")), 1)
assert_eq(r.hget("vehiculo:TEST001", "estado"), "en_uso")
assert_eq(float(r.zscore("ranking:vehiculos:popularidad", "TEST001")), 1.0)
assert r.ttl("reserva:TEST_R001") > 0

# Test 2: Cancelación
pipe = r.pipeline()
pipe.hset("reserva:TEST_R001", "estado", "cancelada")
pipe.hset("vehiculo:TEST001", "estado", "disponible")
pipe.incr("stats:vehiculos:disponibles")
pipe.decr("stats:reservas:activas")
pipe.execute()
assert_eq(r.hget("reserva:TEST_R001", "estado"), "cancelada")
assert_eq(r.hget("vehiculo:TEST001", "estado"), "disponible")
assert_eq(int(r.get("stats:vehiculos:disponibles")), 1)
assert_eq(int(r.get("stats:reservas:activas")), 0)

# Test 3: Cola
r.rpush("queue:test:mantenimiento", "TEST001", "TEST002", "TEST003")
assert_eq(r.llen("queue:test:mantenimiento"), 3)
assert_eq(r.lpop("queue:test:mantenimiento"), "TEST001")
assert_eq(r.llen("queue:test:mantenimiento"), 2)
assert_eq(r.lrange("queue:test:mantenimiento", 0, -1), ["TEST002", "TEST003"])

# Test 4: Ranking
r.zadd("test:ranking", {"V001":100, "V002":200, "V003":150, "V004":180, "V005":120})
assert_eq(r.zrevrange("test:ranking", 0, 2, withscores=True)[0][0], "V002")
r.zincrby("test:ranking", 50, "V001")
assert "V001" in [x[0] for x in r.zrevrange("test:ranking", 0, 3, withscores=True)]
assert set([x[0] for x in r.zrangebyscore("test:ranking", 151, "+inf", withscores=True)]) >= {"V002","V004"}

# Test 5: Sesión con expiración
r.setex("test:session:short", 2, "test_session_data")
assert_eq(r.get("test:session:short"), "test_session_data")
time.sleep(3)
assert_eq(r.get("test:session:short"), None)

# Test 6: Strings y operaciones atómicas
r.set("test:counter", 0)
for _ in range(5):
    r.incr("test:counter")
assert_eq(int(r.get("test:counter")), 5)
r.incrby("test:counter", 10)
assert_eq(int(r.get("test:counter")), 15)
r.decr("test:counter")
assert_eq(int(r.get("test:counter")), 14)
r.append("test:text", "Hola")
r.append("test:text", " Mundo")
assert_eq(r.get("test:text"), "Hola Mundo")
assert_eq(r.strlen("test:text"), 10)

# Test 7: Sets
r.sadd("test:set", "A", "B", "C")
assert_eq(r.sismember("test:set", "A"), 1)
assert_eq(r.scard("test:set"), 3)
r.srem("test:set", "B")
assert_eq(r.smembers("test:set"), {"A", "C"})

# Test 8: Hashes
r.hset("test:hash", mapping={"a": "1", "b": "2"})
assert_eq(r.hget("test:hash", "a"), "1")
r.hincrby("test:hash", "a", 2)
assert_eq(r.hget("test:hash", "a"), "3")
assert_eq(set(r.hkeys("test:hash")), {"a", "b"})

# Test 9: Listas
r.rpush("test:list", "x", "y", "z")
assert_eq(r.lindex("test:list", 1), "y")
r.lpop("test:list")
assert_eq(r.lrange("test:list", 0, -1), ["y", "z"])
r.lpush("test:list", "w")
assert_eq(r.lrange("test:list", 0, -1), ["w", "y", "z"])

# Test 10: Sorted sets avanzados
r.zadd("test:zset", {"a": 1, "b": 2, "c": 3})
assert_eq(r.zrange("test:zset", 0, -1), ["a", "b", "c"])
assert_eq(r.zrevrange("test:zset", 0, 1), ["c", "b"])
r.zrem("test:zset", "b")
assert_eq(r.zrange("test:zset", 0, -1), ["a", "c"])

# Test 11: Expiraciones y persistencia
r.set("test:expire", "bye", ex=2)
assert r.ttl("test:expire") > 0
r.persist("test:expire")
assert_eq(r.ttl("test:expire"), -1)

# Test 12: Tipos de datos
r.set("test:type:str", "v")
r.lpush("test:type:list", "v")
r.sadd("test:type:set", "v")
r.zadd("test:type:zset", {"v": 1})
r.hset("test:type:hash", "f", "v")
assert_eq(r.type("test:type:str"), b'string')
assert_eq(r.type("test:type:list"), b'list')
assert_eq(r.type("test:type:set"), b'set')
assert_eq(r.type("test:type:zset"), b'zset')
assert_eq(r.type("test:type:hash"), b'hash')

# Limpieza final
for key in r.keys("test:*"):
    r.delete(key)
for key in r.keys("queue:test:*"):
    r.delete(key)
for key in r.keys("reserva:TEST_*"):
    r.delete(key)
for key in r.keys("vehiculo:TEST*"):
    r.delete(key)
