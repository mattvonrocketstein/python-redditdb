""" redditdb.topic
"""
from loggable import Loggable
from memoized_property import memoized_property


class TopicBase(Loggable):
    """
    """

    def __init__(self, name=None, reddit=None, **kwargs):
        super(TopicBase, self).__init__(**kwargs)
        self.reddit = reddit
        self.name = name
        err = 'must provide name and reddit'
        assert self.name and self.reddit, err

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<redditdb.Topic {}>'.format(str(self))

    def put(self, key, value):
        raise Exception('niy')

    def __setitem__(self, key, value):
        return self.put(key, value)

    def search(self, query):
        raise Exception('niy')
    # def get(self, key):
    #     return self.data[key]
    # def __getitem__(self, key):
    #     return self.get(key)

    def __iter__(self):
        return iter(self.data.keys())

    @memoized_property
    # def attachments(self):
    def data(self):
        result = {}
        for x in self.obj.comments.list():
            tmp = x.body.split('\n')
            key = tmp.pop(0)
            tmp = '\n'.join(tmp)
            result[key] = json.loads(tmp)
        return result


class Topic(TopicBase):
    """
    """

    def __init__(self, obj=None, **kwargs):
        super(Topic, self).__init__(**kwargs)
        err = 'must provide obj, or else use LazyTopic'
        assert obj is not None, err
        self.obj = obj


class LazyTopic(TopicBase):
    """
    a topic that is not necessarily created or discovered yet
    """

    @property
    def obj(self):
        if hasattr(self, '_obj'):
            return self._obj
        else:
            # get it from self.reddit
            raise Exception('niy')
            self._obj = self.get_toplevel_submission(
                self.name)

    def create(self):
        self._obj = self.reddit.create_toplevel_submission(
            name=self.name)
        return self
