# 기말과제를 위해 정리 중

## Poetry 가상 런타임 프로젝트 폴더 안에 만들기

```shell
poetry config virtualenvs.in-project true
poetry config virtualenvs.path "./.venv"

# 프로젝트 내부에 venv 새로 설치
poetry install && poetry update
```

이렇게 하면 VS Code 등에서 알아서 잡아줌.

## 해야할 일 정리

- [ ] Lark 정리
- [ ] Lexer
  - [x] 토큰 정리
  - [x] 토큰 정규식 작성
  - [ ] 테스트
- [ ] Parser
  - [x] 문법 탐구
  - [ ] Parser 코드 뜯어보기
  - [ ] Grammar Rule 작성
  - [ ] 테스트
- [ ] Transformer
  - [ ] EdgeDB 구조 뜯기
  - [ ] ???

## EdgeQL의 토큰 종류
`edgeql/parser/grammar/tokens.py` 에 토큰 종류가 나옴
`edgeql/parser/grammar/lexer.py` EdgeQLLexer 에 파이썬 코드 및 정규표현식이 있음.
`MULTILINE_TOKENS = frozenset(('SCONST', 'BCONST', 'RSCONST'))` 는 s 플래그를 써서 여러줄을 한 줄처럼 인식할 수 있도록 해야함
이 외에는 imx 플래그를 사용.
`lark_poetry/grammar/tokenize.lark` 에 정리해놓았고 <b>현재 실행 가능</b>

## EdgeQL의 Expression 종류
`gram.md` 참조
`edgeql/parser/grammar/expressions.py` 에 모든 문법이 나옴

다음처럼 생각하면 됨
```python
class ExprStmtCore(Nonterm):
    def reduce_SimpleFor(self, *kids):
        self.val = kids[0].val

    def reduce_SimpleSelect(self, *kids):
        self.val = kids[0].val

    def reduce_SimpleGroup(self, *kids):
        self.val = kids[0].val

    def reduce_InternalGroup(self, *kids):
        self.val = kids[0].val

    def reduce_SimpleInsert(self, *kids):
        self.val = kids[0].val

    def reduce_SimpleUpdate(self, *kids):
        self.val = kids[0].val

    def reduce_SimpleDelete(self, *kids):
        self.val = kids[0].val

class SimpleSelect(Nonterm):
    def reduce_Select(self, *kids):
        r"%reduce SELECT OptionallyAliasedExpr \
                  OptFilterClause OptSortClause OptSelectLimit"

```
equiv. to
```lark
expr_stmt_core : simple_for
              | simple_select
              | simple_group
              | internal_group
              | simple_insert
              | simple_update
              | simple_delete
simple_select : SELECT optionally_aliased_expr opt_filter_clause opt_sort_clause opt_select_limit *

```