from boofuzz import *

def main():

	port = 9999
	host = "10.0.2.6"
	protocol = 'tcp'
	session = Session(
		target=Target(
			connection=SocketConnection("10.0.2.6", 9999, proto='tcp')))

	s_initialize("kstet") # begin of a request and named it as kstet
	s_string("KSTET",fuzzable=False) # first block of request
	s_delim(" ", fuzzable=False) #delimiter between KSTET and value
	s_string("FUZZ") # fuzzing variable
	s_static("\r\n") # final block hits enter for us

	session.connect(s_get("kstet"))
	session.fuzz()

if __name__ == "__main__":
	main()
