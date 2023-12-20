```python exec
import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import docdemo_from, doclink
from pcweb.pages.docs.vars.var_operations import var_operations
```

# Conditional Rendering

We use the `cond` component to conditionally render components. The `cond` component acts in a similar way to a conditional (ternary) operator in python, acting in a similar fashion to an `if-else` statement.


```python eval
rx.alert(
    rx.alert_icon(),
    rx.alert_title("Check out the API reference for ", doclink("cond docs", href="https://reflex.dev/docs/library/layout/cond/")),
    status="info",
)
```
```python eval
rx.box(height="2em")
```

Here is a simple example to show how by checking the value of the state var `show` we can render either `blue` text or `red` text. 

The first argument to the `cond` component is the condition we are checking. Here the condition is the value of the state var boolean `show`. 

If `show` is `True` then the 2nd argument to the `cond` component is rendered, in this case that is `rx.text("Text 1", color="blue")`. 

If `show` is `False` then the 3rd argument to the `cond` component is rendered, in this case that is `rx.text("Text 2", color="red")`.

```python exec
class CondSimpleState(rx.State):
    show: bool = True

    def change(self):
        self.show = not (self.show)


def cond_simple_example():
    return rx.vstack(
        rx.button("Toggle", on_click=CondSimpleState.change),
        rx.cond(
            CondSimpleState.show,
            rx.text("Text 1", color="blue"),
            rx.text("Text 2", color="red"),
        ),
    )
```

```python eval
docdemo_from(CondSimpleState, component=cond_simple_example)
```


## Var Operations (negation)

You can use var operations with the `cond` component. To learn more generally about var operators check out [these docs]({var_operations.path}). The logical operator `~` can be used to negate a condition. In this example we show that by negating the condition `~CondNegativeState.show` within the cond, we then render the `rx.text("Text 1", color="blue")` component when the state var `show` is negative.


```python exec
class CondNegativeState(rx.State):
    show: bool = True

    def change(self):
        self.show = not (self.show)


def cond_negative_example():
    return rx.vstack(
        rx.text(f"Value of state var show: {CondNegativeState.show}", as_="strong"),
        rx.button("Toggle", on_click=CondNegativeState.change),
        rx.cond(
            CondNegativeState.show,
            rx.text("Text 1", color="blue"),
            rx.text("Text 2", color="red"),
        ),
        rx.cond(
            ~CondNegativeState.show,
            rx.text("Text 1", color="blue"),
            rx.text("Text 2", color="red"),
        ),
    )
```

```python eval
docdemo_from(CondNegativeState, component=cond_negative_example)
```


## Multiple Conditions

It is also possible to make up complex conditions using the `logical or` (|) and `logical and` (&) operators. 

Here we have an example using the var operators `>=`, `<=`, `&`. We define a condition that if a person has an age between 18 and 65, including those ages, they are able to work, otherwise they cannot. 

We could equally use the operator `|` to represent a `logical or` in one of our conditions.


```python exec
import random

class CondComplexState(rx.State):
    age: int = 19

    def change(self):
        self.age = random.randint(0, 100)


def cond_complex_example():
    return rx.vstack(
        rx.button("Toggle", on_click=CondComplexState.change),
        rx.text(f"Age: {CondComplexState.age}"),
        rx.cond(
            (CondComplexState.age >= 18) & (CondComplexState.age <=65),
            rx.text("You can work!", color="green"),
            rx.text("You cannot work!", color="red"),
        ),
    )

```

```python eval
docdemo_from(CondComplexState, component=cond_complex_example, imports=["import random"])
```





## Reusing Cond


We can also reuse a `cond` component several times by defining it within a function that returns a `cond`. 

In this example we define the function `render_item`. This function takes in an `item`, uses the `cond` to check if the item `is_packed`. If it is packed it returns the `item_name` with a `✔` next to it, and if not then it just returns the `item_name`.

```python exec
class ToDoListItem(rx.Base):
    item_name: str
    is_packed: bool

class CondRepeatState(rx.State):
    to_do_list: list[ToDoListItem] = [
        ToDoListItem(item_name="Space suit", is_packed=True), 
        ToDoListItem(item_name="Helmet", is_packed=True),
        ToDoListItem(item_name="Back Pack", is_packed=False),
        ]


def render_item(item: [str, bool]):
    return rx.cond(
        item.is_packed, 
        rx.list_item(item.item_name + ' ✔'),
        rx.list_item(item.item_name),
        )

def packing_list():
    return rx.vstack(
        rx.text("Sammy's Packing List", as_="strong"),
        rx.list(rx.foreach(CondRepeatState.to_do_list, render_item)),
    )

```

```python eval
docdemo_from(ToDoListItem, CondRepeatState, render_item, component=packing_list)
```


## Nested Conditional 


We can also nest `cond` components within each other to create more complex logic. In python we can have an `if` statement that then has several `elif` statements before finishing with an `else`. This is also possible in reflex using nested `cond` components. In this example we check whether a number is positive, negative or zero.

Here is the python logic using `if` statements:

```python
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')
```

This reflex code that is logically identical:

```python exec

import random


class NestedState(rx.State):
    
    num: int = 0

    def change(self):
        self.num = random.randint(-10, 10)


def cond_nested_example():
    return rx.vstack(
        rx.button("Toggle", on_click=NestedState.change),
        rx.cond(
            NestedState.num > 0,
            rx.text(f"{NestedState.num} is Positive!", color="orange"),
            rx.cond(
                NestedState.num == 0,
                rx.text(f"{NestedState.num} is Zero!", color="blue"),
                rx.text(f"{NestedState.num} is Negative!", color="red"),
            )
        ),
    )

```

```python eval
docdemo_from(NestedState, component=cond_nested_example, imports=["import random"])
```


Here is a more advanced example where we have three numbers and we are checking which of the three is the largest. If any two of them are equal then we return that `Some of the numbers are equal!`. 

The reflex code that follows is logically identical to doing the following in python:

```python
a = 8
b = 10
c = 2

if((a>b and a>c) and (a != b and a != c)): 
	print(a, " is the largest!") 
elif((b>a and b>c) and (b != a and b != c)): 
	print(b, " is the largest!") 
elif((c>a and c>b) and (c != a and c != b)): 
	print(c, " is the largest!") 
else: 
	print("Some of the numbers are equal!") 
```


```python exec
import random


class CNS(rx.State):
    # CNS: CondNestedState
    a: int = 8
    b: int = 10
    c: int = 2
    

    def change(self):
        self.a = random.randint(0, 10)
        self.b = random.randint(0, 10)
        self.c = random.randint(0, 10)


def cond_nested_example_2():
    return rx.vstack(
        rx.button("Toggle", on_click=CNS.change),
        rx.text(f"a: {CNS.a}, b: {CNS.b}, c: {CNS.c}"),
        rx.cond(
            ((CNS.a > CNS.b) & (CNS.a > CNS.c)) & ((CNS.a != CNS.b) & (CNS.a != CNS.c)),
            rx.text(f"{CNS.a} is the largest!", color="green"),
            rx.cond(
                ((CNS.b > CNS.a) & (CNS.b > CNS.c)) & ((CNS.b != CNS.a) & (CNS.b != CNS.c)),
                rx.text(f"{CNS.b} is the largest!", color="orange"),
                rx.cond(
                    ((CNS.c > CNS.a) & (CNS.c > CNS.b)) & ((CNS.c != CNS.a) & (CNS.c != CNS.b)),
                    rx.text(f"{CNS.c} is the largest!", color="blue"),
                    rx.text("Some of the numbers are equal!", color="red"),
                ),
            ),
        ),
    )

```

```python eval
docdemo_from(CNS, component=cond_nested_example_2, imports=["import random"])
```


## Cond used as a style prop

`Cond` can also be used to show and hide content in your reflex app. In this example, we have no third argument to the `cond` operator which means that nothing is rendered if the condition is false.

```python exec
class CondStyleState(rx.State):
    show: bool = False
    img_url: str = "/preview.png"
    def change(self):
        self.show = not (self.show)


def cond_style_example():
    return rx.vstack(
        rx.button("Toggle", on_click=CondStyleState.change),
        rx.cond(
            CondStyleState.show,
            rx.image(
                src=CondStyleState.img_url,
                height="25em",
                width="25em",
            ),
        ),
    )
```

```python eval
docdemo_from(CondStyleState, component=cond_style_example)
```



