# /usr/bin/python3

"""Scan, Own, Find (SOF) everything wireless on the 2.5 and 5.0 GHz bandwidth

Bluetooth bandwidth support is coming soon, in version, like, 9.0bt
"""

import sys
import os
import subprocess
from subprocess import STDOUT
import re


# TODO: Enuerate system
# Store all information inside RAM
# Everything will need to be recreated upon start-up and will be completely empty and blank to start with,
# but will be the only way to have a system that lives in RAM
# And also self-generating from the very beginning
def system():
    """What is in this system?
    """

    if sys.platform == 'linux':
        return system_start(sys.platform)

    if sys.platform is 'windows':
        return system_start(sys.platform)

    return False


def system_start(platform):
    """Initialize the system and its devices
    """

    if platform == 'windows':
        return Exception('You\'re using Window\'s? Is this a game to you? This only supports Linux')

    if platform == 'linux':
        return wireless()

    return Exception('[Error] Unknown system')


def wireless():
    """These are definitely your wireless devices that you have available for you to use
    Have fun

    :return:
    """

    path, dirlist = devices()

    for device in dirlist:
        for _ in subprocess.check_output('iwconfig'.split(), stderr=STDOUT).splitlines():
            if re.findall('^' + device, _.decode()) and not re.findall('no wireless extensions', _.decode()):
                # TODO: Add support for multiple wireless cards in future
                # Create a list of multiple wireless cards and let the user know

                # TODO: Get wireless device type (a,b,g,n,ac,ad)
                # Depending on the wireless capabilities of the card, pick the one with the most capabilities
                # Use that card to scan on the frequency that none others can. Then use the other cards to
                # scan for the other frequencies

                # TODO: Get wireless device modes that are available
                # If more than one wireless devices, find out what modes it can run in (managed, monitor, master)
                # Use card with master mode as an AP

                return str(device).strip()

    else:
        return Exception('Can\'t find any wireless devices in', path, 'We tested these:', dirlist)


# TODO: Get system wireless devices
# Using iw, and iwconfig to enumerate the wireless devices of the system
def devices():
    """Return either a list of all wireless devices or the best wireless device to use on this excursion
    """

    # TODO: Get wireless devices from iwconfig
    # These should be the network devices that the system knows based on iwconfig

    # TODO: Get wireless devices from ifconfig
    # Possibly match against the devices found in ifconfig

    # TODO: Get wireless devices from dmesg
    # Possibly match what the boot log shows

    # TODO: Get wireless devices from lspci
    # Maybe something here

    # /sys/class/net/
    path = '/sys/class/net/'

    return path, os.listdir(path)


# TODO: Find out all of the wireless stations, bssids around
# The list of all the stations and bssids will be used to create a database, a graph database
def sonar():
    """Get all of the wireless signals around you and the area that you're in
    Let the owning begin
    """

    return


# TODO: Create local graph database
# The local graph database will need to be imported/synced with the main database in some way
def db():
    """All of this data needs a home, it needs to go somewhere, be somewhere
    Mind as well create a relational graph database of everything that's happening around you

    The graph database will need to be synced into the master database (somehow)
    """

    # TODO: Check if database is installed
    # Check if path to neo4j exists

    # TODO: Check if database is running
    # Check if bolt port is available?
    # Try authenticating to bolt port

    # TODO: Start database if it isn't running

    return


# TODO: Integrate local graph database with master graph database
# The system needs to be stateful while offline and remote,
# and capable of syncing all local database findings to the remote master server
def db_sync():
    """If the remote database can be reached, test he connection, and sync the data between both databases in threaded
    real time, if possible

    If the latency between the databases grows, switch back to local-only db

    :return:
    """
    return


def main():
    return print(system())


if __name__ == '__main__':
    main()
