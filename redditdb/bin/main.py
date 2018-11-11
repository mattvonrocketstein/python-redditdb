# -*- coding: utf-8 -*-
""" redditdb.bin.main

    A command-line-interface that demos and
    exercises most of the features available.

    This CLI is used directly in the automated tests
"""

import click
from loggable import get_logger
LOGGER = get_logger(__name__)


@click.group(invoke_without_command=True)
@click.option('--topic', help='set reddit topic name', default='general')
@click.option('--describe-topics', help='describe all topics in reddit', default=False, is_flag=True)
@click.option('--dump-topic', help='dump contents of reddit topic', default=False, is_flag=True)
@click.option('--search', help='search links under given topic (used with --topic)')
@click.option('--set', help='set a value under the given topic (used with --topic)')
@click.option('--get', help='get a value under the given topic (used with --topic)')
@click.pass_context
def entry(ctx, topic, set, get, dump_topic, describe_topics, search, ):
    from redditdb import RedditDB
    db = RedditDB()
    err_topic_required = '--topic must be provided with this command'
    err_value_required = '--value must be provided with this command'
    if describe_topics:
        LOGGER.debug("dispatching for describe-topics")
        result = [x for x in db]
    elif dump_topic:
        assert topic, err_topic_required
        LOGGER.debug("dispatching for dump-topic")
        topic = db[topic]
        LOGGER.debug("got topic: {}".format(topic))
        result = [x for x in topic]
    elif search:
        assert topic, err_topic_required
        LOGGER.debug("dispatching for search")
        result = db[topic_name].search(search)
    elif set_key or get_key:
        assert topic, err_topic_required
        LOGGER.debug("dispatching for get/set")
        if set_key:
            assert value, err_value_required
            result = db[topic_name].set(key, value)
        if get_key:
            result = db[topic_name].get(key)
    print result
    return result
