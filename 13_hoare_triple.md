# Триплы Хоара

{P: любое входное значение x}
Тело функции
```py
def abs(x):
    if x < 0:
        return -x
    return x
```
{Q: результат abs равен |x|}
Доказательство: для ветки x >= 0 значение |x| где x > 0 == x
для ветки x < 0 значение |x| == |-x| == x

{P: любые значения a, b}
Тело функции
```py
def max(a, b):
    if a >= b:
        return a
    return b
```
{Q: значение max(a, b) равно максимальному значению между a и b}
Доказательство: для ветки a >= b возвращается значение a, большее или равное b
                для ветки a <  b возвращается значение b, большее b
Для всех значения a, b возвращается большее значение

{P: 1: abs_a равно значению |a|, 2: abs_b равно |b|, 3: max(a, b) равно максимальному значению между a b }
Тело функции
```py
def max_abs(a, b):
    abs_a = abs(a)
    abs_b = abs(b)
    return max(abs_a, abs_b)
```
{Q: значение max_abs(a, b) равно максимальному значению между модулями a и b}
Доказательство:
- Из (1) следует, что abs_a равно |a|.
- Из (2) следует, что abs_b равно |b|.
- Далее следует, что при подставноки значение max(abs_a, abs_b) равно max(|a|, |b|), как было показаано в (3) возвращает максимум из модулей a и b.
