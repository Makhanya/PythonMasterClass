"""
    Iterators? Iterables?
        Iterator - an object that can be iterated upon. An Object which returns data, one element
            at a time when next() is called on it
        Iterable - An object which will return an Iterator when iter() is called on it

        "Hello" is an iterable, but it is not an iterator
        iter("HELLO") returns an iterator

        NEXT
            When next() is called on an iterator, the iterator returns the next item.
            It keeps doing so until it raises a StopIterator error
"""