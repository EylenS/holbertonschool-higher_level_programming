#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except (ZeroDivisionError) as err:
        print("Exception: {}".format(err), file=sys-sys.stderr)
        return None
    except (IndexError) as err:
        print("Exception: {}".format(err), file=sys-sys.stderr)
        return None
    except (TypeError) as err:
        print("Exception: {}".format(err), file=sys-sys.stderr)
        return None
    except (TypeError) as err:
        print("Exception: {}".format(err), file=sys-sys.stderr)
        return None
