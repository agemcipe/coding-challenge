from collections.abc import Iterable
from typing import Type, TypeVar


# Define Generic Variable Types
A = TypeVar("A")
B =TypeVar("B")


def fold(iterable: Iterable[A], start: B, fn: callable) -> B:
    """Higher Function fold. 

    For details see: https://en.wikipedia.org/wiki/Fold_(higher-order_function)

    Parameters
    ----------
    iterable : Iterable[A]
    start : B
    fn : callable
        Function that combines an element of type B with a sequence of type A

    Returns
    -------
    B
        The result of recursively combining the result of the callable fn with the iterable

    Raises
    ------
    ValueError
        _description_
    """    
    try:
        ls_iter = iter(iterable)
    except:
        raise ValueError(f"Argument iterable of type {type(iterable) } is not iterable")

    def _rec_fold(it, start, fn):
        try: 
            e = next(it)
            return _rec_fold(it, fn(start, e), fn)
        except StopIteration:
            return start

    return _rec_fold(ls_iter, start, fn)        
