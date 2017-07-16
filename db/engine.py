""" Neo4j bolt connector


Written         : Eric Jaw
Version         : 1.0
Created         : 2017-05-27
"""

from neo4j.v1 import GraphDatabase, basic_auth

import os
from sys import stdout, stderr
import subprocess
import threading


def db_start():
    """Start neo4j database
    """

    binary = 'db/neo4j/neo4j-community-3.2.1/bin/neo4j'
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


def run_query(server='bolt://localhost:7687',
              user='neo4j',
              password='redcodes',
              cypher='', close_session=False):
    """ Connect to Neo4j database and start a new session

    :param server: bolt server
    :param user: admin username
    :param password: admin password
    :param cypher: cypher query
    :param close_session: close session boolean
    :return:
    """

    driver = GraphDatabase.driver(server, auth=basic_auth(user, password))
    session = driver.session()

    if close_session is True:
        session.close()

    # print(cypher)

    results = session.run(cypher)  # is a class

    # TODO: print records from cypher response
    # for record in results:
    #     for value in record._values:
    #         for props in value.properties:
    #             print(props, value.properties[props])

    # print(cypher)

    # TODO: print records in JSON format for d3.js

    return results


def main():
    db_start()

if __name__ == '__main__':
    db_start()
