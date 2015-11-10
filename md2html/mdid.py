#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
mdid.py : generate human-friendly IDs for headers in markdown
"""

import argparse
import codecs
from functools import wraps
import logging
import os
import regex as re
import shlex
import sys
import traceback

from slugify import slugify
from nltk.corpus import stopwords

DEFAULTLOGLEVEL = logging.WARNING
RX_HEADER = re.compile(ur'^(?P<hash>#+)\s+(?P<text>((?!{:).)*)\s*({:\s*)?(?P<attrs>((?!\s*}).)*)\s*}?\s*$')
RX_ACRONYM = re.compile(ur'\(([A-Z]+)\)')
RX_SPACES = re.compile(ur'\s+')

STOP_WORDS = stopwords.words("english")

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
        md = sys.stdin.readlines()
    else:
        with codecs.open(infn, 'r', 'utf-8') as f:
            md = f.readlines()

    md_out = []
    for i,line in enumerate(md):
        if line.startswith(u'#'):
            logger.debug(u"line: {0}".format(line))
            heading = RX_HEADER.match(line).groupdict()
            logger.debug(u'heading attrs:\n    {0}'.format(heading.get('attrs')))
            attrs_raw = shlex.split(heading.get('attrs'))
            attrs = {}
            logger.debug(u'attrs_raw:\n    {0}'.format(attrs_raw))

            try:
                attrs['id'] = [a[1:] for a in attrs_raw if a.startswith('#')][0]
            except IndexError:
                attrs['id'] = u''
            attrs['class'] = [a[1:] for a in attrs_raw if a.startswith('.')]
            others = [a for a in attrs_raw if '=' in a]
            logger.debug(u"others:\n    {0}".format(others))
            for other in others:
                logger.debug(u"other:\n    {0}".format(other))
                logger.debug(u"other split:\n    {0}".format(other.split('=')))
                k,v = other.split('=')
                vals = v.split()
                logger.debug(u"splitted:\n    {0}:'{1}'".format(k, v))                
                if k in attrs.keys():
                    attrs[k].extend(vals)
                else:
                    attrs[k] = vals
            logger.debug("attrs:\n    {0}".format(u"\n    ".join([u"{0}:'{1}'".format(k, v) for (k,v) in attrs.iteritems()])))

            logger.debug(u'attrs keys:\n    {0}'.format(u', '.join((attrs.keys()))))
            if len(attrs['id']) == 0:
                m = None
                m = RX_ACRONYM.search(heading['text'])
                if m is not None:
                    attrs['id'] = m.group(1)    # ignores id specs greater than the first
                else:
                    attrs['id'] = heading['text']
                attrs['id'] = u' '.join([word for word in attrs['id'].split() if word not in STOP_WORDS])
                attrs['id'] = slugify(attrs['id'].lower())
                logger.debug(u"created hdr_id='{0}'".format(attrs['id']))
            attribs = u'#{id}'.format(**attrs)
            for k,v in attrs.iteritems():
                if k == 'id':
                    pass
                elif k == 'class' and len(v) > 0:
                    attribs = attribs + u' .' + u' .'.join(v)
            hdr_new = u' '.join((heading['hash'], heading['text'], u'{:', attribs, u'}'))
            if hdr_new != line:
                logger.warning(u"input line {0}: rewrote line as '{1}'".format(i, hdr_new))
            md_out.append(hdr_new)
        else:
            md_out.append(line)

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
