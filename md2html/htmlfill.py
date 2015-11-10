#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
htmlfill.py : insert html content into html template
"""

import argparse
import codecs
from functools import wraps
import logging
import os
import regex as re
import sys
import traceback

import datetime
from dateutil import parser as dateparser
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
    tplfn = args.template_filename
    metafn = args.metadata_filename
    outfn = args.output_filename

    with codecs.open(tplfn, 'r', 'utf-8') as f:
        tpl = f.read()

    replacements = {
        u'title': u'',
        u'creator': u'',
        u'description': u'',
        u'date': u'',
        u'datehuman': u'',
        u'subjects': u'',
        u'dctype': u'Text',
        u'language': u'en-US',
        u'citation': u'',
        u'url': u'',
        u'ogtype': u'article',
        u'ogimage': u'http://pleiades.stoa.org/images/pleiades-social-logo/image'
    }



    if metafn is not None:
        with codecs.open(metafn, 'r', 'utf-8') as f:
            meta = f.readlines()
        for i,line in enumerate(meta):
            if line.strip() == u'':
                break
        if i > 0:
            meta = meta[:i]
            for line in meta:
                k,v = line.split(u':')
                k = k.strip().lower()
                v = v.strip()
                if v == u'':
                    if k == u'date':
                        v = unicode(datetime.datetime.now().isoformat().split(u'T')[0])                    
                if v != u'':
                    if k == u'url':
                        if not v.startswith('http'):
                            v = u'http://pleiades.stoa.org/{0}'.format(v)
                    replacements[k] = v
            if replacements['datehuman'] == u'':
                replacements['datehuman'] = dateparser.parse(replacements['date']).strftime(u'%d %B %Y')
            if replacements['citation'] == u'':
                replacements['citation'] = u'{creator}. &quot;{title}.&quot; Pleiades, {datehuman}. {url}.'.format(**replacements)


    if infn is None:
        sys.stdin = codecs.getreader('utf-8')(sys.stdin)
        html = sys.stdin.read()
    else:
        with codecs.open(infn, 'r', 'utf-8') as f:
            html = f.read()
    replacements[u'content'] = html

    try:
        html = tpl.format(**replacements)
    except KeyError:
        raise

    if outfn is None:
        sys.stdout= codecs.getwriter('utf-8')(sys.stdout)
        sys.stdout.writelines(html)
    else:
        with codecs.open(outfn, 'w', 'utf-8') as f:
            f.writelines(html)


if __name__ == "__main__":
    log_level = DEFAULTLOGLEVEL
    log_level_name = logging.getLevelName(log_level)
    logging.basicConfig(level=log_level)

    try:
        parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument ("-l", "--loglevel", type=str, help="desired logging level (case-insensitive string: DEBUG, INFO, WARNING, ERROR" )
        parser.add_argument ("-v", "--verbose", action="store_true", default=False, help="verbose output (logging level == INFO")
        parser.add_argument ("-vv", "--veryverbose", action="store_true", default=False, help="very verbose output (logging level == DEBUG")
        parser.add_argument ("-i", "--input_filename", type=str, help="html filename to read")
        parser.add_argument ("-o", "--output_filename", type=str, help="html filename to write")
        parser.add_argument ("-t", "--template_filename", type=str, required=True, help="template file to use")
        parser.add_argument ("-m", "--metadata_filename", type=str, help="markdown file containing metadata")
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
