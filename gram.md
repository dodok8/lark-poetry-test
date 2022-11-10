# Grammar
todo: function call, set, shape, path, Evaluation algorithm에 대해 더 잘 보고 여러모로 고치기 
### Select
```lark
select_stmt: [with_blk] "select" expr [filter_cls] [order_cls] [offset_cls] [limit_cls] ";"
```
##### filter, order by, offset, limit
```lark
filter_cls : "filter" filter_expr
filter_expr : expr <bool>

order_cls : "order" "by" order_expr ["asc" | "dsc"] ["empty" ("first"|"last")] ["then"]
order_expr : expr <orderable>

offset_cls : "offset" offset_expr
offset_expr : expr <singleton int>

limit_cls : "limit" limit_expr
limit_expr : expr <singleton int>
```
### Insert
```lark
insert_stmt : [with_blk] "insert" expr [insert_shape] 
              ["unless conflict" ["on" property_expr ["else" alternative]]] ";"
```
#### unless conflict on ~ else ~
```lark
property_expr : expr <property, link, tuple>
alternative : expr
```

### Update
```lark
update_stmt : [with_blk] "update" selector_expr [filter_cls] "set" update_shape ";"
selector_expr : expr <set of objects>
```

### Delete
```lark
delete_stmt : [with_blk] "delete" expr [filter_cls] [order_cls] [offset_cls] [limit_cls] ";"
```

### For
```lark
for_cls : [with_blk] "for" variable "in" iterator_expr "union" output_expr ";"
iterator_expr : expr <literal, function call, set constructor, path>
output_expr : expr
```

### Group
```lark
group_stmt : [with_blk] "group" [alias ":="] expr [using_cls] by_cls ";"
```
#### using, by
```lark
using_cls : "using" using_alias ":=" expr
using_alias : IDENT(아마도 variable계열의 identifier일듯 todo)

by_cls : "by" group_elem
group_elem : ref_or_list | "{" group_elem ["," group_elem]* "}" | (("ROLLUP" | "CUBE") "(" ref_or_list ["," ref_or_list]* ")" )
ref_or_list : "(" ")" | group_ref | "(" group_ref ["," group_ref]* ")"
group_ref : using_alias | "." field_name
field_name : IDENT (todo)
```

### With(todo)
```lark
with_stmt : "with" with_elem [ "," with_elem ]*
with_elem : with_alias ":=" expr | "module" module_name | with_alias "as module" module_name
```
