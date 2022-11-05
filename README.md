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

- [ ] EdgeQL 문법 탐구
- [ ] Lark 정리
- [ ] 토큰 탐구
  - [ ] 키워드 정리
  - [ ] 키워드가 아닌 토큰 종류 정리
  - [ ] 문법 정리

## EdgeQL의 토큰 종류

`edgeql-parser/src/tokenizer.rs` 에 정리가 되어 있음.

```rust
pub const MAX_KEYWORD_LENGTH: usize = 16;


#[cfg_attr(feature="wasm-bindgen",
    wasm_bindgen::prelude::wasm_bindgen(js_name=TokenKind))]
#[cfg_attr(feature="wasm-bindgen", derive(serde::Serialize))]
#[derive(Debug, PartialEq, Eq, Clone, Copy, Hash)]
pub enum Kind {
    Assign,           // :=
    SubAssign,        // -=
    AddAssign,        // +=
    Arrow,            // ->
    Coalesce,         // ??
    Namespace,        // ::
    BackwardLink,     // .<
    FloorDiv,         // //
    Concat,           // ++
    GreaterEq,        // >=
    LessEq,           // <=
    NotEq,            // !=
    NotDistinctFrom,  // ?=
    DistinctFrom,     // ?!=
    Comma,            // ,
    OpenParen,        // (
    CloseParen,       // )
    OpenBracket,      // [
    CloseBracket,     // ]
    OpenBrace,        // {
    CloseBrace,       // }
    Dot,              // .
    Semicolon,        // ;
    Colon,            // :
    Add,              // +
    Sub,              // -
    Mul,              // *
    Div,              // /
    Modulo,           // %
    Pow,              // ^
    Less,             // <
    Greater,          // >
    Eq,               // =
    Ampersand,        // &
    Pipe,             // |
    At,               // @
    Argument,         // $something, $`something`
    DecimalConst,
    FloatConst,
    IntConst,
    BigIntConst,
    BinStr,           // b"xx", b'xx'
    Str,              // "xx", 'xx', r"xx", r'xx', $$xx$$
    BacktickName,     // `xx`
    Substitution,     // \(name)
    Keyword,
    Ident,
}
```

Ident는 뭐지?

키워드도 `keyword.rs` 파일에 정리가 되어 있음. 이건 너무 길긴 한데, 어쨋든 현재 예약된 단어 정도만 활용하면 될 것 같음.

이들을 바탕으로 현재 단어가 키워드인지 아닌지 판별하는 함수가 토큰나이저 안에 있음. 근데 이것도 우리가 구현이 필요한지 의문임.