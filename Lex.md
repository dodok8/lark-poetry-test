# Lexical Structure
Keyword, Identifier, Literal, Symbol 로 구성됨.
세미콜론으로 끝남.

## Identifier
```lark
identifier : plain_ident | quoted_ident
plain_ident : /[a-zA-Z_][a-zA-Z0-9_]*/
quoted_ident : /`(?!::)[^@]((?!::).)*`/
```