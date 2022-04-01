from element import Element
import copy

hydrogen = Element('H', 1, 1.01, 1)
h = copy.copy(hydrogen)
h_ref = hydrogen
print(h)
print(hydrogen)
print(h_ref)
print(h.__doc__)