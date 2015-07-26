import pdb
import types
class C:
    pass

def f(self):
    print self

a = C()

pdb.set_trace()

a.f = types.MethodType(f,a)
a.f()

pdb.set_trace()

