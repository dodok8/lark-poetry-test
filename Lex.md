# Lexical Structure
Keyword, Identifier, Literal, Symbol 로 구성됨.
세미콜론으로 끝남.

## 공식코드에서 추출한 렉서 룰들
```lark
# STATE_KEEP으로 이어짐
WS : /[^\S\n]+/x
NL : "\n"
COMMENT : /\#.*?$/ix

#Keyword
KEYWORD : /\bblahblah\b/x
짱많음...

#Symbol
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
self : /[\{\}]/x

#Literal
NFCONST : / (?: (?: \d+ (?:\.\d+)? (?:[eE] (?:[+\-])? [0-9]+ ) ) | (?: \d+\.\d+)) n /x   # decimal 표현
NICONST : / ((?:[1-9]\d* | 0)n) /x # Bigint 표현
FCONST : / (?: \d+ (?:\.\d+)? (?:[eE](?:[+\-])?[0-9]+) ) | (?: \d+\.\d+) /x # Float 표현
ICONST  : / ([1-9]\d* | 0)(?![0-9]) /x
BCONST : / (?:b) (?P<BQ> ' | ") (?: (\\\\ | \\['"] | \n | .)*? ) (?P=BQ) /mx # Byte string(multiline)
RSCONST : / (?: r)? (?P<RQ> (?: (?<=r) (?: ' | ") ) | (?: (?<!r) (?: \$ (?: [A-Za-z_][A-Za-z_0-9]*)? \$ )) ) (?: (\n | .)*? )(?P=RQ) /mx # raw string (dollar string 포함, multiline)
SCONST :  / (?P<Q> ' | " ) (?: ( \\\\ | \\['"] | \n | . )*? ) (?P=Q) /mx # 일반 string, multiline

#Identifier
IDENT : /[^\W\d]\w*/x # 일반 식별자
QIDENT : /`([^`]|``)*/x # quoted 식별자
ARGUMENT : /\$(?:[0-9]+|[^\W\d]\w*|`(?:[^`]|``)*`)/x # 외부에서 입력하는 args

#Convenient Error Only
BADSCONST : /[rb]?(['"] | (?: \$(?:[A-Za-z_][A-Za-z_0-9]*)?\$))[^\n]*/mx
BADIDENT : /__[^\W\d]\w*__|`__([^`]|``)*__`(?!`)/x
BADARGUMENT : /\$[0-9]+[^\W\d]\w*/x

UNKNOWN : /./
```
