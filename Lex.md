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
```
## 공식코드에서 추출한 렉서 룰들
```lark
# STATE_KEEP으로 이어짐
[키워드(대문자)] : /\bblahblah\b/x
WS : /[^\S\n]+/x
NL : "\n"
COMMENT : /\#.*?$/x

ASSIGN : ":="
REMASSIGN : "-="
ADDASSIGN : "+="
ARROW : "->"
COALESCE : "??"
FULLQUAL : "::"
BACKLINK : ".<"
FLOORDIV : "//"
CONCAT : "++"
OP : / (?: >= | <= | != | \?= | \?!=) /x
self : / [,()\[\].@;:+\-*/%^<>=&|] /x

NFCONST : / (?: (?: \d+ (?:\.\d+)? (?:[eE] (?:[+\-])? [0-9]+ ) ) | (?: \d+\.\d+)) n /x   # decimal 표현
NICONST : / ((?:[1-9]\d* | 0)n) /x # Bigint 표현
FCONST : / (?: \d+ (?:\.\d+)? (?:[eE](?:[+\-])?[0-9]+) ) | (?: \d+\.\d+) /x # Float 표현
ICONST  : / ([1-9]\d* | 0)(?![0-9]) /x
BCONST : / (?:b) (?P<BQ> ' | ") (?: (\\\\ | \\['"] | \n | .)*? ) (?P=BQ) /mx # Byte string(multiline)
RSCONST : / (?: r)? 
            (?P<RQ>
                (?: (?<=r) (?: ' | ") ) 
                |
                (?: (?<!r) (?: \$ (?: [A-Za-z_][A-Za-z_0-9]*)? \$ ))
            )
            (?: (\n | .)*? )
            (?P=RQ) /mx # raw string (dollar string 포함, multiline)
SCONST :  / (?P<Q> ' | " ) (?: ( \\\\ | \\['"] | \n | . )*? ) (?P=Q) /mx # 일반 string, multiline

IDENT : /[^\W\d]\w*/x # 일반 식별자
QIDENT : /`([^`]|``)*/x # quoted 식별자
self : /[\{\}]/x 
ARGUMENT : /\$(?:[0-9]+|[^\W\d]\w*|`(?:[^`]|``)*`)/x # 외부에서 입력하는 args

BADSCONST : /[rb]?(['"] | (?: \$(?:[A-Za-z_][A-Za-z_0-9]*)?\$))[^\n]*/mx
BADIDENT : /__[^\W\d]\w*__|`__([^`]|``)*__`(?!`)/x
BADARGUMENT : /\$[0-9]+[^\W\d]\w*/x

UNKNOWN : /./
```
