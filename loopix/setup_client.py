import core
import sys
import os.path
import petlib.pack


if __name__ == "__main__":

	port = int(sys.argv[1])
	host = sys.argv[2]
	name = sys.argv[3]
	prvinfo = str(sys.argv[4])
        local_path = "/volumes/global/publicClient-" + host + ".bin"

	if not (os.path.exists("secretClient.prv") and os.path.exists("publicClient.bin") and os.path.exists(local_path)):

		setup = core.setup()
		G, o, g, o_bytes = setup

		secret = o.random()
		file("secretClient.prv", "wb").write(petlib.pack.encode(secret))

		pub = secret * g
		file("publicClient.bin", "wb").write(petlib.pack.encode(["client", name, port, host, pub, prvinfo]))
		file(local_path, "wb").write(petlib.pack.encode(["client", name, port, host, pub, prvinfo]))
	else:
		print "Files exist"
