import sys
import core
import petlib.pack
import os.path
import time
import os
import sqlite3
import petlib
import time


if __name__ == "__main__":

	num = int(sys.argv[1])
        sys.path += ["/app"]
        os.chdir('/volumes/global')
        if os.path.exists("example.db"):
            os.remove("example.db")
        if os.path.exists("Controller_done"):
            os.remove("Controller_done")

        #import databaseConnect as dc
        from database_connect import DatabaseManager
        databaseName = "example.db"
        dbManager = DatabaseManager(databaseName)
        dbManager.create_users_table("Users")
        dbManager.create_providers_table("Providers")
        dbManager.create_mixnodes_table("Mixnodes")
        while True:
            time.sleep(1)
            c = 0 
            for f in os.listdir('.'):
                c += 1
            if c >= num:
                break

        for f in os.listdir('.'):
            if f.endswith(".bin"):
                with open(f, 'rb') as fileName:
                    lines = petlib.pack.decode(fileName.read())
                    print 'Lines: ', lines
                    if lines[0] == "client":
                        dbManager.insert_row_into_table('Users',
                            [None, lines[1], lines[2], lines[3],
                            sqlite3.Binary(petlib.pack.encode(lines[4])),
                            lines[5]])
                    elif lines[0] == "mixnode":
                        dbManager.insert_row_into_table('Mixnodes',
                                [None, lines[1], lines[2], lines[3],
                                sqlite3.Binary(petlib.pack.encode(lines[5])), lines[4]])
                    elif lines[0] == "provider":
                        dbManager.insert_row_into_table('Providers',
                            [None, lines[1], lines[2], lines[3],
                            sqlite3.Binary(petlib.pack.encode(lines[4]))])
                    else:
                        assert False
        dbManager.close_connection()
        file("Controller_done", "wb").write("done")
