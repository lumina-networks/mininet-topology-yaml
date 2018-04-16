from mn_topo.core.utility import merge_two_dicts, u_to_ascii


def test_merge_two_dicts():
    a = { 'a':1,'b':2 }
    b = { 'c':1,'d':2 }
    c = { 'a':3,'b':4 }
    x = merge_two_dicts(a,b)
    y = merge_two_dicts(a, c)
    z = merge_two_dicts(c, a)
    assert x == { 'a':1,'b':2,'c':1,'d':2 }
    assert y == {'a': 3, 'b': 4}
    assert z == {'a': 1, 'b': 2}


def test_u_to_ascii():
    assert 'test' == u_to_ascii(u'test')