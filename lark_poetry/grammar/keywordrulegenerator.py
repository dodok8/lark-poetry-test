reserved_keyword = ["AGGREGATE",  "ALTER",  "AND",  "ANY",  "COMMIT",  "CREATE",  "DELETE",  "DETACHED",  "DISTINCT",  "DROP",  "ELSE",  "EMPTY",  "EXISTS",  "FALSE",  "FILTER",  "FUNCTION",  "GET",  "GROUP",  "IF",
                    "ILIKE",  "IN",  "INSERT",  "IS",  "LIKE",  "LIMIT",  "MODULE",  "NOT",  "OFFSET",  "OR",  "ORDER",  "OVER",  "PARTITION",  "ROLLBACK",  "SELECT",  "SET",  "SINGLETON",  "START",  "TRUE",  "UPDATE",  "UNION",  "WITH"]

unreserved_keyword = ["ABSTRACT",  "ACTION",  "AFTER",  "ARRAY",  "AS",  "ASC",  "ATOM",  "ANNOTATION",  "BEFORE",  "BY",  "CONCEPT",  "CONSTRAINT",  "DATABASE",  "DESC",  "EVENT",  "EXTENDING",  "FINAL",  "FIRST",
                      "FOR",  "FROM",  "INDEX",  "INITIAL",  "LAST",  "LINK",  "MAP",  "MIGRATION",  "OF",  "ON",  "POLICY",  "PROPERTY",  "REQUIRED",  "RENAME",  "TARGET",  "THEN",  "TO",  "TRANSACTION",  "TUPLE",  "VALUE",  "VIEW"]


for s in unreserved_keyword:
    print(s.upper()+".6" + " : /\\b"+s+"\\b/i")

print(" | ".join(unreserved_keyword))
