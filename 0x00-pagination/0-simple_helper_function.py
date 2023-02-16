#!/usr/bin/env python3
""" defines a function index_range"""


def index_range(page: int, page_size: int) -> tuple:
    """ return a tuple of size two containing a start and end index"""
    pg = page * page_size
    return (pg - page_size, page * page_size)
