#!/usr/bin/python3

"""Start me up and see where things go
"""

import iw.wireless
import db.engine
import threading


if __name__ == '__main__':
    threading.Thread(target=iw.wireless.main()).start()

    # TODO: bug - Thread is blocking
    threading.Thread(target=db.engine.main()).start()
