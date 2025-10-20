# Python DevOps S-0

## Onboarding homework tasks

### Task 1 List statistics

**Description:**
Write a function `list_stats(numbers: list[int]) -> dict` that receives a list of integers and returns a dictionary with keys: `min`, `max`, `sum`, `avg` (rounded to 2 decimals), and `unique_count`.

**Example:**
Input: `[3, 5, 3, 10, -1]`
Output: `{"min": -1, "max": 10, "sum": 20, "avg": 4.00, "unique_count": 4}`

**Requirements / notes:**

* Use loops (no built-in `min`/`max`/`sum` for the main logic).
* Handle empty list by raising a `ValueError` with a clear message.

**Acceptance:** correct values for example; raises `ValueError` for `[]`.

---

### Task 2 Filter and transform strings

**Description:**
Write `filter_transform(words: list[str], min_len: int) -> list[str]` that returns a new list with words longer than `min_len`, converted to lowercase and sorted alphabetically.

**Example:**
Input: `(["Hello", "to", "WORLD", "py"], 2)`
Output: `["hello", "world"]`

**Requirements / notes:**

* Use iteration and branching to select items.
* Do not use `filter()` or `map()` (explicit loops preferred).

**Acceptance:** output matches example and is sorted.

---

### Task 3 Word frequency (use regex)

**Description:**
Write `top_words(text: str, n: int = 3) -> list[tuple[str,int]]` that finds words in `text` (case-insensitive), counts their occurrences, and returns the top `n` words with counts as `(word, count)` tuples. Use a regular expression to extract words (letters and digits allowed).

**Example:**
Input: `("Hello, hello! This is a test. Test; test?", 2)`
Output: `[("test", 3), ("hello", 2)]`

**Requirements / notes:**

* Normalize words to lowercase.
* Use `re` to extract tokens.
* Ties can be broken by alphabetical order.

**Acceptance:** example result and correct counting.

---

### Task 4 Simple email validator (regex + branching)

**Description:**
Write `validate_emails(emails: list[str]) -> dict` that separates the input into `{"valid": [...], "invalid": [...]}` using a simple regex for email format (local@domain). Do basic checks: one `@`, domain contains at least one `.`, no spaces.

**Example:**
Input: `["user@example.com", "bad@@x", "no-at-sign.com"]`
Output: `{"valid": ["user@example.com"], "invalid": ["bad@@x", "no-at-sign.com"]}`

**Requirements / notes:**

* Use `re` to validate; do not require full RFC compliance — a simple, practical pattern is enough.
* If input is not a list, raise `TypeError`.

**Acceptance:** correct separation for example; raises `TypeError` for non-list input.

---

### Task 5 Robust number parser and summation (exceptions)

**Description:**
Write `sum_numbers_from_lines(lines: list[str]) -> float` which accepts lines each containing a single number possibly with commas or spaces (e.g., `"1,234.56"`). Parse each line to `float`, ignore blank lines, and return the total sum. If a line cannot be parsed, record the line index and continue; after processing raise a single custom `ParseError` listing failed indices **only if** there was at least one parse failure; otherwise return the sum.

**Example:**
Input: `["100", " 2,500.5 ", "", "abc", "3.5"]`
Behavior: parse 100, 2500.5, skip blank, fail on index 3, parse 3.5 → raise `ParseError([3])` after processing.

**Requirements / notes:**

* Implement a custom exception `ParseError` that stores failed indices.
* Use try/except; do not stop on first error.

**Acceptance:** correct sum behavior and `ParseError` contains failed indices when needed.

---

### Task 6 Parentheses balance checker (collections + loops)

**Description:**
Write `is_balanced(s: str) -> bool` that checks whether parentheses `()`, brackets `[]`, and braces `{}` in the string `s` are balanced and properly nested. Ignore other characters.

**Example:**
Input: `"{[()]}()"` → `True`
Input: `"(unbalanced]"` → `False`

**Requirements / notes:**

* Use a stack (list) to track openings.
* Return `True` or `False`, do not raise exceptions.

**Acceptance:** correct boolean for examples and other basic cases.
