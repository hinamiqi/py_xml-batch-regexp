# test1.txt
|Find           |Replace        |Total|
|---------------|---------------|-----|
| Table\s[^\s]* | test_table | 2 |
| Figure\s[^\s]* | test_figure | 1 |
| [0-9]+[^\s]* | test_digits | 0 |
| (\w+)([a-z]) | eng: "\1" | 3 |
| [а-я]+[^\s] | Заменено | 0 |

# test2.txt
|Find           |Replace        |Total|
|---------------|---------------|-----|
| Table\s[^\s]* | test_table | 0 |
| Figure\s[^\s]* | test_figure | 0 |
| [0-9]+[^\s]* | test_digits | 2 |
| (\w+)([a-z]) | eng: "\1" | 2 |
| [а-я]+[^\s] | Заменено | 0 |

# test3.txt
|Find           |Replace        |Total|
|---------------|---------------|-----|
| Table\s[^\s]* | test_table | 2 |
| Figure\s[^\s]* | test_figure | 2 |
| [0-9]+[^\s]* | test_digits | 4 |
| (\w+)([a-z]) | eng: "\1" | 11 |
| [а-я]+[^\s] | Заменено | 30 |

# Topic_test_1.txt
|Find           |Replace        |Total|
|---------------|---------------|-----|
| Table\s[^\s]* | test_table | 0 |
| Figure\s[^\s]* | test_figure | 0 |
| [0-9]+[^\s]* | test_digits | 1 |
| (\w+)([a-z]) | eng: "\1" | 1 |
| [а-я]+[^\s] | Заменено | 4 |

