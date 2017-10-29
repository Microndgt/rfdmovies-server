rfdmovies-server
================

instant recommending or finding or downloading movies via the command line
--------------------------------------------------------------------------

It's server code deployed at Tencent Cloud. The server will answer the clients' requests and make response.

Installation
------------

install pyssdb first:`pip install git+https://github.com/Microndgt/pyssdb_customized.git`

`git clone https://github.com/Microndgt/rfdmovies-server.git`

Usage
-----

- start server: `inv web.server`
- start celery: `inv web.celery`

API
---

[API文档]()

Note
----

- Base on `Flask + Celery + gunicorn`
