<table>
  <tr><th><strong>python-redditdb</strong></th>
    <th style="padding:0px 5px;text-align:right;float:right;">
      <small><small>
      <a href=#overview>Overview</a> |
      <a href=#overview>Design</a> |
      <a href=#prerequisites>Prerequisites</a> |
      <a href=#usage>Usage</a> |
      <a href=#running-tests>Running Tests</a> |
      <a href=#related-work>Related Work</a>
      </small><small>
    </th>
  </tr>
  <tr>
    <td width=15%><img src=img/icon.png style="width:150px"></td>
    <td>
    This is a library that can help crazy people treat a subreddit as a persistent storage backend / document store.  This is, of course, a horrible idea.  This whole thing should be considered an interesting toy at best.
    </td>
  </tr>
</table>

## Overview

This is a library that can help crazy people treat a subreddit as a persistent storage backend / document store.  This is, of course, a horrible idea.  This whole thing should be considered an interesting toy at best, and nothing about it is efficient.  Besides, Reddit will probably kick you off pretty quickly if you do anything at volume.

## Design

This implementation maps *top-level posts on the subreddit* to "topics", aka what is simply called "databases" in other infrastructure like PG, Redis, or Mongo.  Topics are namespaces and do not directly store key/values, but organize them.  

Individual *key/value pairs* are mapped to comments underneath top-level posts.  Keys are simply strings, values are JSON.  

Of course in theory it's straightforward to extend this library to store anything you can serialize, so go nuts.  A key/value store piggy-backing on a comment forum is crazy, but a object database would be even more nuts..

## Prerequisites

#### Reddit User

You need at least a registered script client id/secret from reddit.  See also the documentation provided by praw library [here](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application).  You could set this script client id/secret up so that they are attached to your personal reddit user, but you probably just want a dedicated robot user.

#### Reddit Subreddit  

You also need a subreddit already setup for the data backend, probably one that is private and dedicated to this whole thing.  Posts that do not use the storage-backend data format can be ignored, but this is even more ridiculously inefficient because they have to be parsed first to determine that they should be ignored.

The reddit user you setup in the last step should also be a moderator for this subreddit.  (This is because sticky-thread features are used to control top-level post sorting)

#### Local Dotfiles

It's optional to do things this way, but you may want to manage configuration details outside of your code.  This library supports dot-env files natively via the [pydotenv library](#).  If the library is used from a working directory that includes a `.env` the contents will automatically loaded into `os.environ` on your behalf.  

All of the expected/supported environment variables are included below

```
REDDIT_USER=myuser
REDDIT_PASSWORD=mypassword
REDDIT_CLIENT_ID=myid
REDDIT_CLIENT_SECRET=mysecret
REDDIT_SUBREDDIT=example
```

## Usage

```
from redditdb import RedditDB

# if you're using .env, or otherwise setting up the environment  
# variables you can instantiate the database with no arguments at all.
db = RedditDB()

# or, provide all the details directly to the constructor
db = RedditDB(subreddit='..', client_id='..', client_secret='..', username='..', password='..')

# creates `topic_name` if it doesn't already exist
db[topic_name][key] = value
db[topic_name].put(key, value)

# get a key
db[topic_name][key]
db[topic_name].get(key)

# destructive get
db[topic_name].pop(key)

# deletes topic (and all associated keys)
del db[topic_name]
db[topic_name].delete()
```

## Running Tests

Placeholder
