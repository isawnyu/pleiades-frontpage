#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
htmlpretty.py : prettify html
"""

import argparse
import codecs
from functools import wraps
import logging
import os
import regex as re
import sys
import traceback

from lxml import etree

DEFAULTLOGLEVEL = logging.WARNING

def normalize_whitespace(s):
    s = s.strip()
    s = RX_SPACES.sub(u' ', s)
    return s

def arglogger(func):
    """
    decorator to log argument calls to functions
    """
    @wraps(func)
    def inner(*args, **kwargs): 
        logger = logging.getLogger(func.__name__)
        logger.debug("called with arguments: %s, %s" % (args, kwargs))
        return func(*args, **kwargs) 
    return inner    


@arglogger
def main (args):
    """
    main functions
    """
    logger = logging.getLogger(sys._getframe().f_code.co_name)

    infn = args.input_filename
    outfn = args.output_filename

    if infn is None:
        sys.stdin = codecs.getreader('utf-8')(sys.stdin)
        html = sys.stdin.read()
    else:
        with codecs.open(infn, 'r', 'utf-8') as f:
            html = f.read()

    html = html.encode('utf-8')
    parser = etree.XMLParser(remove_blank_text=True)
    soup = etree.fromstring(html, parser=parser)
    pretty = etree.tounicode(soup, method='xml', pretty_print=True)

    if outfn is None:
        sys.stdout= codecs.getwriter('utf-8')(sys.stdout)
        sys.stdout.writelines(pretty)
    else:
        with codecs.open(outfn, 'w', 'utf-8') as f:
            f.writelines(pretty)


if __name__ == "__main__":
    log_level = DEFAULTLOGLEVEL
    log_level_name = logging.getLevelName(log_level)
    logging.basicConfig(level=log_level)

    try:
        parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument ("-l", "--loglevel", type=str, help="desired logging level (case-insensitive string: DEBUG, INFO, WARNING, ERROR" )
        parser.add_argument ("-v", "--verbose", action="store_true", default=False, help="verbose output (logging level == INFO")
        parser.add_argument ("-vv", "--veryverbose", action="store_true", default=False, help="very verbose output (logging level == DEBUG")
        parser.add_argument ("-i", "--input_filename", type=str, help="markdown filename to read")
        parser.add_argument ("-o", "--output_filename", type=str, help="markdown filename to write")
        # example positional argument:
        # parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
        args = parser.parse_args()
        if args.loglevel is not None:
            args_log_level = re.sub('\s+', '', args.loglevel.strip().upper())
            try:
                log_level = getattr(logging, args_log_level)
            except AttributeError:
                logging.error("command line option to set log_level failed because '%s' is not a valid level name; using %s" % (args_log_level, log_level_name))
        if args.veryverbose:
            log_level = logging.DEBUG
        elif args.verbose:
            log_level = logging.INFO
        log_level_name = logging.getLevelName(log_level)
        logging.getLogger().setLevel(log_level)
        if log_level != DEFAULTLOGLEVEL:
            logging.warning("logging level changed to %s via command line option" % log_level_name)
        else:
            logging.info("using default logging level: %s" % log_level_name)
        logging.debug("command line: '%s'" % ' '.join(sys.argv))
        main(args)
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print "ERROR, UNEXPECTED EXCEPTION"
        print str(e)
        traceback.print_exc()
        os._exit(1)
