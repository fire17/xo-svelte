import time
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room, leave_room
# from xo import *
from xo.redis import xoRedis
# import eventlet
# from eventlet import wsgi
# eventlet.monkey_patch()

redis = xoRedis()
port = 5000
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins=['http://localhost:8080','http://localhost:5173','http://localhost:4173'],async_mode='threading')

redis.count = 11

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    redis.lastSession = request.sid # type: ignore
    print('A user connected', redis.lastSession)

@socketio.on('disconnect')
def on_disconnect():
    print('A user disconnected', request.sid) # type: ignore

@socketio.on('user_msg')
def on_send_message(message):
    print(f'Received message: {message}')

    # Send message back to the client that initiated the event
    # redis.sessions[request.sid].message = message
    print(":::",request.__dir__)
    # emit('server_update', {"data":message+"!","message":message+"@@"}, room = request.sid)
    emit('server_update', {"data":{"_value":"{'Server Recieved': {message:'"+message+"'}}","extra":{"_value":"inner_data","meta":{}}},"message":str(message)+"!"}, room = request.sid)  # type: ignore
    print(":::",request.sid)  # type: ignore
    # print(xo)
    # redis.lastSession = request.sid

    # send('server_update', message+"!", room=request.sid)

# redis.trigger.on = "off"

# @socketio.on('disconnect')
def manualCount(*v,**kw):
    print("count transfer",v, kw)
    room = redis.lastSession.value  # type: ignore
    # socketio.emit('server_update', {"message":"countTransfer","count":int(v[0])}, to = room)
    # socketio.emit('server_update', {"data":{"_value":v[0],"extra":{"_value":"inner_data","meta":{}}},"message":str(v[0]),"count":int(redis.count.value)}, to = room)
    socketio.emit('server_update', {"data":{"_value":f"{v[0]}","extra":{"_value":"inner_data","meta":{}}},"message":str(v[0]),"count":int(v[0])}, to = room)
            
def manual(*v,**kw):
    print("!!!!!!!!!!!!!!",v, kw)
    redis.trigger.on.value  # type: ignore
    print("starting manual", str(redis.tigger.on.value), str(redis.tigger.on) == "on")  # type: ignore
    if str(redis.tigger.on.value) == "on":  # type: ignore
        print("Running manual",v, kw)
        emit('server_update', {"data":v}, to = redis.lastSession.value)  # type: ignore
        print("done emmiting to", redis.lastSession.value )  # type: ignore
    else:
        print("....",redis.trigger.on.value, type(redis.trigger.on.value), redis.trigger.on.value == "on")  # type: ignore
        if redis.trigger.on.value == "on":  # type: ignore
            print("YYYYYY")
            print("Running manual",v, kw)
            room = redis.lastSession.value  # type: ignore
            print("xxxxxxxxxxxxxxxxxxxx trying  emmiting to", room , redis.lastSession.value ) # type: ignore
            # socketio.emit('server_update', {"data":"aaaaaa"}, room = room)
            
            if True:
                # socketio.emit('server_update', {"data":v[0],"message":str(v[0])+"@@"}, to = room)
                socketio.emit('server_update', {"data":{"_value":f"Server Sent: {v[0]}","extra":{"_value":"inner_data","meta":{}}},"message":str(v[0]),"count":int(redis.count.value)}, to = room)  # type: ignore
                # socketio.emit('server_update', {"data":{"_value":message+"@","extra":{"_value":"inner_data","meta":{}}},"message":str(message)+"@@"}, room = request.sid)

            else:
                c = 0
                while(c<100):
                    socketio.emit('server_update', {"data":f"{v[0]} {c}"}, to = room)
                    time.sleep(redis.settings.delay.value)
                    c+=1
                    print("c....",c)
            # socketio.send('server_update', {"data":"cccccccccc"}, to = room)
            # socketio.call('server_update', {"data":"xxxxxxxxxxxx"}, room = room, namespace='/test')
            # socketio.send({"data":"ooooooo"},json = True, =room)
            print("done emmiting to", redis.lastSession.value ) # type: ignore
        else:
            print("XXXXXXXXXX")

redis.trigger @= lambda *v, **kw : manual(*v,**kw) # type: ignore
redis.count @= lambda *v, **kw : manualCount(*v,**kw) # type: ignore



if __name__ == '__main__':
    socketio.run(app, debug=True)
    # wsgi.server(eventlet.listen(('0.0.0.0', port)), app)
