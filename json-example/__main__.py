from lark import Lark

json_parser = Lark.open("json.lark", rel_to=__file__, start="value")
text = '{"key": ["item0", "item1", 3.14, true]}'
print(json_parser.parse(text).pretty())
