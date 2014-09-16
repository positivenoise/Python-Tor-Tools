import socket
import urllib2
import socks

def checkTorIP():

	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, "127.0.0.1", 9050, True)
	socket.socket = socks.socksocket
	req = urllib2.Request("http://whatismyip.com.au/")
	response = urllib2.urlopen(req)
	html = response.read()
	start = html.find("<title>") + 49
	end = html.find("; By DomainHost.com.au</title>")
	print html[start:end].strip()	

def renewTorIdentity(passAuth):

    s = socket.socket()
    s.connect(('localhost', 9051))
    s.send('AUTHENTICATE "{0}"\r\n'.format(passAuth))
    resp = s.recv(1024)

    if resp.startswith('250'):
        s.send("signal NEWNYM\r\n")
        resp = s.recv(1024)

        if resp.startswith('250'):
            return True

    return False
	
