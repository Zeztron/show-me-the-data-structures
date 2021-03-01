## Least Recently Used Cache

I managed to use ``OrderedDict`` from the ``collections`` package.
Using this package keeps order of insertion of keys which can be changed once that is required. The ``get()`` and ``set()`` methods both have a Time Complexity of constant time O(1) which is a huge advantage of using the OrderedDict. The ``move_to_end(key)`` method provided by OrderedDict is also a convenient method that moves the provided key to the end of the dict. This operation is also constant time.

For ``get(key)`` we can return the value of the key which is O(1). It'll return -1 if the key is not found. We also have to move the key to the end using ``move_to_end(key)``

For ``set(key, value)`` we have to first add the key and also move the key to the end to show that it was recently used with ``move_to_end(key)``. We have to check if the length of the OrderedDict is greater than the total capacity... if it is - we remove the first key (which is the least recently used key)