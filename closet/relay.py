import machine
import socket

SENSOR  = machine.Pin(0, machine.Pin.IN)
SWITCH0 = machine.Pin(2, machine.Pin.OUT)
SWITCH1 = machine.Pin(4, machine.Pin.OUT)

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>Ronja's Closet</title> </head>
<body>
<center><h2>Ronja's Closet Controller</h2></center>
<form>
LED0:
<button name="SWITCH1" value="ON1" type="submit">SWITCH 1 ON</button>
<button name="SWITCH1" value="OFF1" type="submit">SWITCH 1 OFF</button><br><br>
</form>
</body>
</html>"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    SWITCHON1 = request.find('/?SWITCH1=ON1')
    SWITCHOFF1 = request.find('/?SWITCH1=OFF1')

    if SWITCHON1 == 6:
        print('TURN SWITCH 1 ON')
        SWITCH1.on()
    if SWITCHOFF1 == 6:
        print('TURN SWITCH 1 OFF')
        SWITCH1.off()

    response = html
    conn.send(response)
    conn.close()
