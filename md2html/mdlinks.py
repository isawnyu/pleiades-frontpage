#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
mdlinks.py : link helpers for faster markdown
"""

import argparse
import codecs
from functools import wraps
import logging
import os
import regex as re
import sys
import traceback

from slugify import slugify

DEFAULTLOGLEVEL = logging.WARNING
RX_BARELINK = re.compile(ur'(?<!\])[\[\(](https?:\/\/[^\s\]\)]+)[\]\)](?!\()')
RX_BAREEMAIL = re.compile(ur'(?<!\])[\[\(]([\p{L&}\p{Nd}!#\$%&\'\*\+-/=\?\^_`\{\|}~\.]+@[\p{L&}\p{Nd}\.]+(\?subject=[\p{L&}\p{Nd}\s]+)?)[\]\)](?!\()')

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
        md = sys.stdin.readlines()
    else:
        with codecs.open(infn, 'r', 'utf-8') as f:
            md = f.readlines()

    md_out = []
    m = None
    for i,line in enumerate(md):
        m = RX_BARELINK.search(line)
        new_line = line
        while (m is not None):
            logger.warning(u"input line {0}: rewriting bare link {1}".format(i, m.group(1)))
            new_line = new_line[:m.start()] + u'[{0}]({0})'.format(m.group(1)) + new_line[m.end():]
            m = RX_BARELINK.search(new_line)
        m = RX_BAREEMAIL.search(new_line)
        while (m is not None):
            logger.warning(u"input line {0}: rewriting bare email as mailto link {1}".format(i, m.group(1)))
            if u'?subject=' in m.group(1):
                new_line = new_line[:m.start()] + u'[{0}](mailto:{1})'.format(m.group(1).split('?subject')[0], m.group(1)) + new_line[m.end():]
            else:
                new_line = new_line[:m.start()] + u'[{0}](mailto:{0})'.format(m.group(1)) + new_line[m.end():]
            m = RX_BAREEMAIL.search(new_line)
        md_out.append(new_line)

    if outfn is None:
        sys.stdout= codecs.getwriter('utf-8')(sys.stdout)
        sys.stdout.writelines(md_out)
    else:
        with codecs.open(outfn, 'w', 'utf-8') as f:
            f.writelines(md_out)


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
