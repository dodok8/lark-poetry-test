from lark import Lark

l = Lark('''start: WORD "," WORD "!"
            %import common.WORD   // imports from terminal library
            %ignore " "           // Disregard spaces in text
        ''')

print(__file__)
eql = Lark.open('grammar/grammar.lark', rel_to=__file__, parser="lalr")

print(l.parse("Hello, World!"))
print(eql.parse("create create"))
