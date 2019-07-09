import time

cnt = 1
while True:
    print( "Hello! #{}".format( cnt ) )
    if cnt >= 10:
        break
    cnt = cnt + 1
    time.sleep(1.0)
