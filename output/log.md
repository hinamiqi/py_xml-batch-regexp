# test1.txt
1. Table\s[^\s]* -> test_table | 2
2. Figure\s[^\s]* -> test_figure | 1
3. [0-9]+[^\s]* -> test_digits | 0
4. (\w+)([a-z]) -> eng: "\1" | 3

# filename
|Find           |Replace        |Total|
|---------------|---------------|-----|
| Table\s[^\s]* | test_table | 2 |
| Figure\s[^\s]* | test_figure | 1 |
| [0-9]+[^\s]* | test_digits | 0 |
| (\w+)([a-z]) | eng: "\1" | 3 |

# test2.txt
1. Table\s[^\s]* -> test_table | 0
2. Figure\s[^\s]* -> test_figure | 0
3. [0-9]+[^\s]* -> test_digits | 2
4. (\w+)([a-z]) -> eng: "\1" | 2

# filename
|Find           |Replace        |Total|
|---------------|---------------|-----|
| Table\s[^\s]* | test_table | 0 |
| Figure\s[^\s]* | test_figure | 0 |
| [0-9]+[^\s]* | test_digits | 2 |
| (\w+)([a-z]) | eng: "\1" | 2 |

# test3.txt
1. Table\s[^\s]* -> test_table | 2
2. Figure\s[^\s]* -> test_figure | 2
3. [0-9]+[^\s]* -> test_digits | 4
4. (\w+)([a-z]) -> eng: "\1" | 11

# filename
|Find           |Replace        |Total|
|---------------|---------------|-----|
| Table\s[^\s]* | test_table | 2 |
| Figure\s[^\s]* | test_figure | 2 |
| [0-9]+[^\s]* | test_digits | 4 |
| (\w+)([a-z]) | eng: "\1" | 11 |

