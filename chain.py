#!/usr/bin/env python

import functools


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper


@coroutine
def char_handler(successor=None):
    while True:
        request = (yield)
        if request.isalpha():
            print 'request {} handled in char_handler'.format(request)
        elif successor is not None:
            successor.send(request)


@coroutine
def digit_handler(successor=None):
    while True:
        request = (yield)
        if request.isdigit():
            print 'request {} handled in digit_handler'.format(request)
        elif successor is not None:
            successor.send(request)


def main():
    requests = ['a', '55']
    pipeline = char_handler(digit_handler())

    for request in requests:
        pipeline.send(request)


if __name__ == '__main__':
    main()
