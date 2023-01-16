import core
import sys
import petlib.pack
import os.path

if __name__ == "__main__":

        port = int(sys.argv[1])
        host = sys.argv[2]
        name = sys.argv[3]

        local_path = "/volumes/global/publicProvider-" + host + ".bin"
	if not (os.path.exists("secretProvider.prv") and os.path.exists("publicProvider.bin") and os.path.exists(local_path)):

		setup = core.setup()
		G, o, g, o_bytes = setup

		secret = o.random()
		file("secretProvider.prv", "wb").write(petlib.pack.encode(secret))

		pub = secret * g
		file("publicProvider.bin", "wb").write(petlib.pack.encode(["provider", name, port, host, pub]))
		file(local_path, "wb").write(petlib.pack.encode(["provider", name, port, host, pub]))
	else:
		print "Files Exist"
