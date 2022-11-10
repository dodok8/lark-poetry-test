# Lexical Structure
Keyword, Identifier, Literal, Symbol 로 구성됨.
세미콜론으로 끝남.

## Identifier
```lark
identifier : plain_ident | quoted_ident
plain_ident : /^[a-zA-Z_]\w*$/
quoted_ident : /^`(?!@)((?!::).)*`$/
```
## Name/Keyword
```lark
short_name : not_keyword_ident | quoted_ident
not_keyword_ident : /((?!^aggregate$)(?!^alter$)(......)))^[a-zA-Z_]\w*$/
keyword : reserved_keyword | unreserved_keyword
reserved_keyword : "AGGREGATE"i | "ALTER"i | "AND"i | "ANY"i | "COMMIT"i | "CREATE"i | "DELETE"i | "DETACHED"i | "DISTINCT"i | "DROP"i | "ELSE"i | "EMPTY"i | "EXISTS"i | "FALSE"i | "FILTER"i | "FUNCTION"i | "GET"i | "GROUP"i | "IF"i | "ILIKE"i | "IN"i | "INSERT"i | "IS"i | "LIKE"i | "LIMIT"i | "MODULE"i | "NOT"i | "OFFSET"i | "OR"i | "ORDER"i | "OVER"i | "PARTITION"i | "ROLLBACK"i | "SELECT"i | "SET"i | "SINGLETON"i | "START"i | "TRUE"i | "UPDATE"i | "UNION"i | "WITH"i
unreserved_keyword : "ABSTRACT"i | "ACTION"i | "AFTER"i | "ARRAY"i | "AS"i | "ASC"i | "ATOM"i | "ANNOTATION"i | "BEFORE"i | "BY"i | "CONCEPT"i | "CONSTRAINT"i | "DATABASE"i | "DESC"i | "EVENT"i | "EXTENDING"i | "FINAL"i | "FIRST"i | "FOR"i | "FROM"i | "INDEX"i | "INITIAL"i | "LAST"i | "LINK"i | "MAP"i | "MIGRATION"i | "OF"i | "ON"i | "POLICY"i | "PROPERTY"i | "REQUIRED"i | "RENAME"i | "TARGET"i | "THEN"i | "TO"i | "TRANSACTION"i | "TUPLE"i | "VALUE"i | "VIEW"i
name : short_name | fq_name
fq_name : short_name "::" short_name | short_name "::" unreserved_keyword
```
## Constants
```lark
string : str | raw_str
str : "'" str_content* "'" | '"' str_content* '"'
