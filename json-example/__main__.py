from lark import Lark, Transformer

json_parser = Lark.open("json.lark", rel_to=__file__, start="value")
text = '{"key": ["item0", "item1", 3.14, true]}'


class MyTransformer(Transformer):
    def list(self, items):
        return list(items)

    def pair(self, key_value):
        k, v = key_value
        return k, v

    def dict(self, items):
        return dict(items)


class TreeToJson(Transformer):
    def string(self, s):
        (s,) = s
        return s[1:-1]

    def number(self, n):
        (n,) = n
        return float(n)

    list = list
    pair = tuple
    dict = dict

    def null(self, _): return None
    def true(self, _): return True
    def false(self, _): return False


tree = json_parser.parse(text)

print(tree.pretty())
print(MyTransformer().transform(tree))
print(TreeToJson().transform(tree))
