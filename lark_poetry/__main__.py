from lark import Lark


l = Lark('''start: WORD "," WORD "!"
            %import common.WORD   // imports from terminal library
            %ignore " "           // Disregard spaces in text
        ''')

print(__file__)
eql = Lark.open('grammar/tokenize.lark', rel_to=__file__,
                parser="lalr")

for tok in Lark.lex(eql,
                    r'''
                    select Movie {
                        title,
                        release_year,
                        actors: {
                            name,
                            `asdfwowna@me`,
                            "asdf{}asdf",
                            @character_name  # link property
                        }
                    }
                    filter .title = "Black Widow";
                                        '''):
    print(tok.type, ': ', tok)
