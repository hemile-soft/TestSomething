.. _api:

API Documentation
=================

This part covers all interfaces you need to implement your own algorithms.


Trying to include a module inside some subpackage. Now, it should work..

``test_something.common.things``

.. automodule:: test_something.common.things


.. autoclass:: test_something.common.things.ClassA
   :members:

.. autofunction:: test_something.common.things.module_function



TestSomething Interface
-----------------------

All functions of the TestSomething module.

This is the ``testsomething.do_something()`` function:

.. py:function:: do_something(arg1: str)

   Return an iterator that yields tuples of an index and an item of the
   *sequence*.

   :param arg1: Optional argument.
   :type arg1: str


.. autofunction:: testsomething.funny_function

.. autofunction:: testsomething.another_function

.. autofunction:: io.open

