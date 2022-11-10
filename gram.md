# Grammar

### Select
```lark
select_stmt: [with_blk] "select" expr [filter_cls] [order_cls] [offset_cls] [limit_cls] ";"
```
##### filter, order by, offset, limit
```
filter_cls : "filter" filter_expr
filter_expr : expr <bool>

order_cls : "order by" order_expr ["asc" | "dsc"] ["empty" ("first"|"last")] ["then"]
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
##### unless conflict on ~ else ~
insert conflict handler (insert 실패를 막지는 못함)
```lark
property_expr : expr <property, link, tuple>
alternative : expr
```

### Update
```lark
update_stmt : [with_blk] "update" selector_expr [filter_cls] "set" shape ";"
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
##### using, by
```lark
using_cls : "using" using_alias ":=" expr
using_alias : ?????????

by_cls : "by" group_elem
group_elem : ?????????
```

### With
```lark
with_stmt : "with" expr
```