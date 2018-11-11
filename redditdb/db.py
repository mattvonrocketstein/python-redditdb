""" redditdb.db
"""
import os
import praw
from memoized_property import memoized_property

from loggable import Loggable
from .topic import Topic, LazyTopic


class RedditDB(Loggable):
    def __init__(self, subreddit=None, client_id=None, client_secret=None, username=None, password=None, **kwargs):
        super(RedditDB, self).__init__(**kwargs)
        self.subreddit_name = subreddit or os.environ['REDDIT_SUBREDDIT']
        self.client_id = client_id or os.environ['REDDIT_CLIENT_ID']
        self.client_secret = client_secret or os.environ['REDDIT_CLIENT_SECRET']
        self.reddit_username = username or os.environ['REDDIT_USER']
        self.reddit_password = password or os.environ['REDDIT_PASSWORD']

    @memoized_property
    def reddit_client(self):
        """ """
        self.debug('getting reddit client')
        return praw.Reddit(
            user_agent='python',
            client_id=self.client_id,
            client_secret=self.client_secret,
            username=self.reddit_username,
            password=self.reddit_password)

    @memoized_property
    def subreddit(self):
        """ """
        return self.reddit_client.subreddit(self.subreddit_name)

    def __iter__(self):
        """ return toplevel submissions """
        for topic in self.subreddit.new(limit=1024):
            yield self.get(topic.title, obj=topic)

    def get(self, topic_name, **kwargs):
        """ """
        obj = kwargs.get('obj')
        kwargs['reddit'] = self
        if not obj:
            self.debug("returning (lazy) topic: {}".format(topic_name))
            return LazyTopic(name=topic_name, **kwargs)
        else:
            self.debug("returning topic: {}".format(topic_name))
            return Topic(name=topic_name, **kwargs)

    def __getitem__(self, topic_name):
        return self.get(topic_name)

    def _create_toplevel_submission(self, name=None,
                                    body=None, send_replies=False,
                                    distinguish=False, sticky=False):
        submission = self.subreddit.submit(
            name, selftext=body, send_replies=send_replies)
        if distinguish:
            submission.mod.distinguish()
        if sticky:
            submission.mod.sticky()
        return submission
