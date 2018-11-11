""" redditdb.topic
"""


class Topic(Loggable):

    def __init__(self, name=None, reddit=None, data=None):
        self.name = name
        self.reddit = reddit
        assert self.name and self.reddit

    def put(self, key, value):
        raise NotImplemented

    def get(self, key):
        raise NotImplemented

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

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


class LazyTopic(Topic):
    """ a topic that is not necessarily created yet """

    def create(self):
        topic = self.reddit.create_toplevel_submission(
            name=self.name)
        return Topic(reddit=self.reddit, name=self.name)
