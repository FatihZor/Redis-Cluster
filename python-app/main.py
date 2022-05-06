from redis import Sentinel
from redis.exceptions import TimeoutError
from redis.sentinel import MasterNotFoundError
from time import sleep

sentinel_nodes = [('localhost', 26379),
            ('localhost', 26380),
            ('localhost', 26381)]

while True:
    sentinel = Sentinel(sentinels=sentinel_nodes, socket_timeout=10)
    try:
        current_master = sentinel.discover_master('master-redis') 
        print("Current Master: ", current_master)

        master = sentinel.master_for('master-redis', socket_timeout=10)
        write_result = master.set('foo', 'bar')
        print(write_result)

        slave = sentinel.slave_for('master-redis', socket_timeout=10)
        read_result = slave.get('foo')
        print(read_result)

    except TimeoutError:
        print("TimeoutError")
        sleep(5)
        continue

    except MasterNotFoundError:
        print("MasterNotFound")
        sleep(10)
        continue

    sleep(5)