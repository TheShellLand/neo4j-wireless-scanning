from neo4j.v1 import GraphDatabase, basic_auth

import os
from sys import stdout, stderr
import subprocess
from subprocess import PIPE
import threading
from queue import Queue
import multiprocessing

q = Queue()


# TODO: Need to add multiprocessing support
# The database cannot run as a separate thread, because it will hang?
# So the database should be run as a separate process
def db_start():
    """Start neo4j database
    """

    binary = 'neo4j/neo4j-community-3.2.1/bin/neo4j'
    params = ' console &'
    run = binary + params

    if os.path.exists(binary):
        # Ensure neo4j binary is executable
        try:
            os.chmod(binary, 0o555)
        except:
            raise

        # Run neo4j
        def neo4j_start():
            p = subprocess.Popen(run.split(), stdout=stdout, stderr=stderr).communicate()
            # p = subprocess.Popen(run.split(), stdout=PIPE, stderr=PIPE).communicate()
            # p = subprocess.check_output(run.split(), stderr=stdout)

        t = threading.Thread(target=neo4j_start())
        t.start()

        return True
    else:
        return False


db_start()
print('Done')
