# Learnings

These are certain *miscellaneous* notes on python. The aim is not to capture everything learned in the course, but to note down certain curious aspects that I wouldn't notice or remember otherwise.

## if...elif

Like bash, python uses `elif`, not `else if`.

```python
if a > 10:
    print("big")
elif a < 5:
    print("not so")
else:
    pass
```

## division, integer division

python (atleast recent versions) divides numbers correctly and produces floats even when dividing integers. `10/3` produces `3.33333`. Unlike in some other languages, we don't have to pass it as `10.0/3` to get the correct result. This makes sense since a dynamically typed language like python should be transparent about the number types. It's justified if a statically typed language returns a rounded (floored) int as a result of division, and the developer is responsible to know that, but not in a dynamically typed language.

That said, python also has a *Floor Divide* operator `//`

```
>>> 10/3
3.3333333333333335
>>> 10//3
3
```
