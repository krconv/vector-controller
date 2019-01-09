from . import controller

import anki_vector

import sys


def main():
    try:
        controller.run()
    except KeyboardInterrupt as e:
        pass
    except anki_vector.exceptions.VectorConnectionException as e:
        sys.exit("A connection error occurred: %s" % e)