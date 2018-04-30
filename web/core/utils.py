import time

from flask import request


def convert_timestamp(dt):
	return time.mktime(dt.timetuple())

def make_cache_key(*args, **kwargs):
    path = request.path
    args = str(hash(frozenset(request.args.items())))
    # lang = get_locale()
    return (path + args).encode('utf-8')

def cache_get_key(resource_cls):
    """ Decorator for adding resources to Api App """
    resource_cls.get.make_cache_key = make_cache_key
    return resource_cls