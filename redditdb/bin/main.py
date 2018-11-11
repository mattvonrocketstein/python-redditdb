# -*- coding: utf-8 -*-
""" redditdb.bin.main

    A command-line-interface that demos and 
    exercises most of the features available.

    This CLI is used directly in the automated tests
"""

import click
from loggable import get_logger
LOGGER = get_logger()


@click.group(invoke_without_command=True)
@click.option('--topic', help='set reddit topic name', default='general')
@click.option('--describe-topics', help='describe all topics in reddit', default=False, is_flag=True)
@click.option('--dump-topic', help='dump contents of reddit topic', default=False, is_flag=True)
@click.option('--search', help='search links under given topic (used with --topic)')
@click.pass_context
def entry(ctx, topic, dump_topic, describe_topics, search, ):
    from redditdb import RedditDB
    db = RedditDB()
    if describe_topics:
        LOGGER.debug("dispatching for describe-topics")
        result = [x for x in db]
    elif dump_topic:
        err = '--topic must be provided with --dump-topic'
        assert topic, err
        LOGGER.debug("dispatching for dump-topic")
        topic = db[topic]
        LOGGER.debug("got topic: {}".format(topic))
        result = [x for x in topic]
    elif search:
        err = '--topic must be provided with --search'
        assert topic, err
        LOGGER.debug("dispatching for search")
        result = db[topic_name].search(search)
    print result
    return result
