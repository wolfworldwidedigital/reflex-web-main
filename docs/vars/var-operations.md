```python exec
import inspect
import random
import time

import numpy as np

import reflex as rx

from pcweb.base_state import State
from pcweb.templates.docpage import (
    doccode,
    docdemo_from,
    docheader,
    doclink,
    docpage,
    doctext,
)
```

# Var Operations

Var operations transform the placeholder representation of the value on the
frontend and provide a way to perform basic operations on the Var without having
to define a computed var.

Within your frontend components, you cannot use arbitrary Python functions on
the state vars. For example, the following code will **not work.**

```python
class State(rx.State):
    number: int

def index():
    # This will be compiled before runtime, before `State.number` has a known value.
    # Since `float` is not a valid var operation, this will throw an error.
    rx.text(float(State.number))
```
This is because we compile the frontend to Javascript, but the value of `State.number`
is only known at runtime.


In this example below we use a var operation to concatenate a `string` with a `var`, meaning we do not have to do in within state as a computed var.

```python exec
coins = ["BTC", "ETH", "LTC", "DOGE"]

class VarSelectState(State):
    selected: str = "DOGE"

def var_operations_example():
    return rx.vstack(
        # Using a var operation to concatenate a string with a var.
        rx.heading("I just bought a bunch of " + VarSelectState.selected),
        # Using an f-string to interpolate a var.
        rx.text(f"{VarSelectState.selected} is going to the moon!"),
        rx.select(
            coins,
            value=VarSelectState.selected,
            on_change=VarSelectState.set_selected,
        )
    )
```

```python eval
docdemo_from(VarSelectState, component=var_operations_example, assignments={"coins": coins})
```

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Vars support many common operations."),
        rx.alert_description(
            "They can be used for arithemtic, string concatenation, inequalities, indexing, and more. "
            "See the ",
            doclink(
                "full list of supported operations",
                "/docs/api-reference/var",
            ),
            ".",
        ),
    ),
    status="success",
    margin_bottom="3em",
)
```




## Supported Operations

Var operations allow us to change vars on the front-end without having to create more computed vars on the back-end in the state.

Some simple examples are the `==` var operator, which is used to check if two vars are equal and the `to_string()` var operator, which is used to convert a var to a string.

```python exec

fruits = ["Apple", "Banana", "Orange", "Mango"]

class EqualsState(State):
    selected: str = "Apple"
    favorite: str = "Banana"


def var_equals_example():
    return rx.vstack(
        rx.text(EqualsState.favorite.to_string() + "is my favorite fruit!"),
        rx.select(
            fruits,
            value=EqualsState.selected,
            on_change=EqualsState.set_selected,
        ),
        rx.cond(
            EqualsState.selected == EqualsState.favorite,
            rx.text("The selected fruit is equal to the favorite fruit!"),
            rx.text("The selected fruit is not equal to the favorite fruit."),
        ),
    )

```

```python eval
docdemo_from(EqualsState, component=var_equals_example, assignments={"fruits": fruits})
```

### Negate, Absolute and Length

The `-` operator is used to get the negative version of the var. The `abs()` operator is used to get the absolute value of the var. The `.length()` operator is used to get the length of a list var.


```python exec
import random

class OperState(State):
    number: int
    numbers_seen: list = []
    def update(self):
        self.number = random.randint(-100, 100)
        self.numbers_seen.append(self.number)

def var_operation_example():
    return rx.vstack(
        rx.heading(f"The number: {OperState.number}", size="md"),
        rx.hstack(
            rx.text("Negated:", rx.badge(-OperState.number, variant="subtle", color_scheme="green")), 
            rx.text(f"Absolute:", rx.badge(abs(OperState.number), variant="subtle", color_scheme="blue")),
            rx.text(f"Numbers seen:", rx.badge(OperState.numbers_seen.length(), variant="subtle", color_scheme="red")),
        ),
        rx.button("Update", on_click=OperState.update),
    )
```

```python eval
docdemo_from(OperState, component=var_operation_example, imports=["import random"])
```

### Comparisons and Mathematical Operators

All of the comparison operators are used as expected in python. These include `==`, `!=`, `>`, `>=`, `<`, `<=`. 

There are operators to add two vars `+`, subract two vars `-`, multiply two vars `*` and raise a var to a power `pow()`.

```python exec
import random

class CompState(State):
    number_1: int
    number_2: int

    def update(self):
        self.number_1 = random.randint(-10, 10)
        self.number_2 = random.randint(-10, 10)

def var_comparison_example():
    
    return rx.vstack(
        rx.table_container(
            rx.table(
                headers=["Integer 1", "Integer 2", "Operation", "Outcome"],
                rows=[
                    (CompState.number_1, CompState.number_2, "Int 1 == Int 2", f"{CompState.number_1 == CompState.number_2}"),
                    (CompState.number_1, CompState.number_2, "Int 1 != Int 2", f"{CompState.number_1 != CompState.number_2}"),
                    (CompState.number_1, CompState.number_2, "Int 1 > Int 2", f"{CompState.number_1 > CompState.number_2}"),
                    (CompState.number_1, CompState.number_2, "Int 1 >= Int 2", f"{CompState.number_1 >= CompState.number_2}"),
                    (CompState.number_1, CompState.number_2, "Int 1 < Int 2 ", f"{CompState.number_1 < CompState.number_2}"),
                    (CompState.number_1, CompState.number_2, "Int 1 <= Int 2", f"{CompState.number_1 <= CompState.number_2}"),
                    (CompState.number_1, CompState.number_2, "Int 1 + Int 2", f"{CompState.number_1 + CompState.number_2}"),
                    (CompState.number_1, CompState.number_2, "Int 1 - Int 2", f"{CompState.number_1 - CompState.number_2}"),
                    (CompState.number_1, CompState.number_2, "Int 1 * Int 2", f"{CompState.number_1 * CompState.number_2}"),
                    (CompState.number_1, CompState.number_2, "pow(Int 1, Int2)", f"{pow(CompState.number_1, CompState.number_2)}"),
                ],
                variant="striped",
                color_scheme="teal",
            ),
        ),
        rx.button("Update", on_click=CompState.update),
    )
```

```python eval
docdemo_from(CompState, component=var_comparison_example, imports=["import random"])
```

### True Division, Floor Division and Remainder

The operator `/` represents true division. The operator `//` represents floor division. The operator `%` represents the remainder of the division.

```python exec
import random

class DivState(State):
    number_1: float = 3.5
    number_2: float = 1.4

    def update(self):
        self.number_1 = round(random.uniform(5.1, 9.9), 2)
        self.number_2 = round(random.uniform(0.1, 4.9), 2)

def var_div_example():
    return rx.vstack(
        rx.table_container(
            rx.table(
                headers=["Integer 1", "Integer 2", "Operation", "Outcome"],
                rows=[
                    (DivState.number_1, DivState.number_2, "Int 1 / Int 2", f"{DivState.number_1 / DivState.number_2}"),
                    (DivState.number_1, DivState.number_2, "Int 1 // Int 2", f"{DivState.number_1 // DivState.number_2}"),
                    (DivState.number_1, DivState.number_2, "Int 1 % Int 2", f"{DivState.number_1 % DivState.number_2}"),
                    ],
                variant="striped",
                color_scheme="red",
            ),
        ),
        rx.button("Update", on_click=DivState.update),
    )
```

```python eval
docdemo_from(DivState, component=var_div_example, imports=["import random"])
```


### And, Or and Not

In Reflex the `&` operator represents the logical AND when used in the front end. This means that it returns true only when both conditions are true simultaneously. 
The `|` operator represents the logical OR when used in the front end. This means that it returns true when either one or both conditions are true.
The `~` operator is used to invert a var. It is used on a var of type `bool` and is equivalent to the `not` operator.

```python exec
import random

class LogicState(State):
    var_1: bool = True
    var_2: bool = True

    def update(self):
        self.var_1 = random.choice([True, False])
        self.var_2 = random.choice([True, False])

def var_logical_example():
    return rx.vstack(
        rx.table_container(
            rx.table(
                headers=["Var 1", "Var 2", "Operation", "Outcome"],
                rows=[
                    (f"{LogicState.var_1}", f"{LogicState.var_2}", "Logical AND (&)", f"{LogicState.var_1 & LogicState.var_2}"),
                    (f"{LogicState.var_1}", f"{LogicState.var_2}", "Logical OR (|)", f"{LogicState.var_1 | LogicState.var_2}"),
                    (f"{LogicState.var_1}", f"{LogicState.var_2}", "The invert of Var 1 (~)", f"{~LogicState.var_1}"),
                    ],
                variant="striped",
                color_scheme="green",
            ),
        ),
        rx.button("Update", on_click=LogicState.update),
    )
```

```python eval
docdemo_from(LogicState, component=var_logical_example, imports=["import random"])
```

### Contains, Reverse and Join


The 'in' operator is not supported for Var types, we must use the `Var.contains()` instead. When we use `contains`, the var must be of type: `dict`, `list`, `tuple` or `str`. 
`contains` checks if a var contains the object that we pass to it as an argument.

We use the `reverse` operation to reverse a list var. The var must be of type `list`.

Finally we use the `join` operation to join a list var into a string. 

```python exec
class ListsState(State):
    list_1: list = [1, 2, 3, 4, 6]
    list_2: list = [7, 8, 9, 10]
    list_3: list = ["p","y","t","h","o","n"]

def var_list_example():
    return rx.hstack(
        rx.vstack(
            rx.heading(f"List 1: {ListsState.list_1}", size="md"),
            rx.text(f"List 1 Contains 3: {ListsState.list_1.contains(3)}"),
        ),
        rx.vstack(
            rx.heading(f"List 2: {ListsState.list_2}", size="md"),
            rx.text(f"Reverse List 2: {ListsState.list_2.reverse()}"),
        ),
        rx.vstack(
            rx.heading(f"List 3: {ListsState.list_3}", size="md"),
            rx.text(f"List 3 Joins: {ListsState.list_3.join()}"),
        ),
    )
```

```python eval
docdemo_from(ListsState, component=var_list_example)
```



### Lower, Upper, Split

The `lower` operator converts a string var to lowercase. The `upper` operator converts a string var to uppercase. The `split` operator splits a string var into a list.

```python exec
class StringState(State):
    string_1: str = "PYTHON is FUN"
    string_2: str = "react is hard"
   

def var_string_example():
    return rx.hstack(
        rx.vstack(
            rx.heading(f"List 1: {StringState.string_1}", size="md"),
            rx.text(f"List 1 Lower Case: {StringState.string_1.lower()}"),
        ),
        rx.vstack(
            rx.heading(f"List 2: {StringState.string_2}", size="md"),
            rx.text(f"List 2 Upper Case: {StringState.string_2.upper()}"),
            rx.text(f"Split String 2: {StringState.string_2.split()}"),  
        ),
    )
```

```python eval
docdemo_from(StringState, component=var_string_example)
```


## Get Item (Indexing)

Indexing is only supported for strings, lists, tuples, dicts, and dataframes. To index into a state var strict type annotations are required.

```python
class GetItemState1(State):
    list_1: list = [50, 10, 20]

def get_item_error_1():
    return rx.vstack(
        rx.circular_progress(value=GetItemState1.list_1[0])
    )
```


In the code above you would expect to index into the first index of the list_1 state var. In fact the code above throws the error: `Invalid var passed for prop value, expected type <class 'int'>, got value of type typing.Any.` This is because the type of the items inside the list have not been clearly defined in the state. To fix this you change the list_1 defintion to `list_1: list[int] = [50, 10, 20]`

```python exec
class GetItemState1(State):
    list_1: list[int] = [50, 10, 20]

def get_item_error_1():
    return rx.vstack(
        rx.circular_progress(value=GetItemState1.list_1[0])
    )
```

```python eval
docdemo_from(GetItemState1, component=get_item_error_1)
```


### Using with Foreach

Errors frequently occur when using indexing and `foreach`. 

```python
class ProjectsState(rx.State):
    projects: List[dict] = [
        {
            "technologies": ["Next.js", "Prisma", "Tailwind", "Google Cloud", "Docker", "MySQL"]
        },
        {
            "technologies": ["Python", "Flask", "Google Cloud", "Docker"]
        }
    ]

def get_badge(technology: str) -> rx.Component:
    return rx.badge(technology, variant="subtle", color_scheme="green")

def project_item(project: dict):

    return rx.box(
        rx.hstack(            
            rx.foreach(project["technologies"], get_badge)
        ),
    )
```
The code above throws the error `TypeError: Could not foreach over var of type Any. (If you are trying to foreach over a state var, add a type annotation to the var.)`

We must change `projects: list[dict]` => `projects: list[dict[str, list]]` because while projects is annotated, the item in project["technologies"] is not.



```python exec
class ProjectsState(rx.State):
    projects: list[dict[str, list]] = [
        {
            "technologies": ["Next.js", "Prisma", "Tailwind", "Google Cloud", "Docker", "MySQL"]
        },
        {
            "technologies": ["Python", "Flask", "Google Cloud", "Docker"]
        }
    ]


def projects_example() -> rx.Component:
    def get_badge(technology: str) -> rx.Component:
        return rx.badge(technology, variant="subtle", color_scheme="green")

    def project_item(project: dict) -> rx.Component:

        return rx.box(
            rx.hstack(            
                rx.foreach(project["technologies"], get_badge)
            ),
        )
    return rx.box(rx.foreach(ProjectsState.projects, project_item))
```

```python eval
docdemo_from(ProjectsState, component=projects_example)
```


The previous example had only a single type for each of the dictionaries `keys` and `values`. For complex multi-type data, you need to use a `Base var`, as shown below.

```python exec

class ActressType(rx.Base):
    actress_name: str
    age: int
    pages: list[dict[str, str]]

class MultiDataTypeState(rx.State):
    """The app state."""
    actresses: list[ActressType] = [
        ActressType(
            actress_name="Ariana Grande",
            age=30,
            pages=[
                {"url": "arianagrande.com"}, {"url": "https://es.wikipedia.org/wiki/Ariana_Grande"}
            ]
        ),
        ActressType(
            actress_name="Gal Gadot",
            age=38,
            pages=[
                {"url": "http://www.galgadot.com/"}, {"url": "https://es.wikipedia.org/wiki/Gal_Gadot"}
            ]
        )
    ] 

def actresses_example() -> rx.Component:
    def showpage(page: dict[str, str]):
        return rx.vstack(
            rx.text(page["url"]),
        )

    def showlist(item: ActressType):
        return rx.vstack(
            rx.hstack(
                rx.text(item.actress_name),
                rx.text(item.age),
            ),
            rx.foreach(item.pages, showpage),
        )
    return rx.box(rx.foreach(MultiDataTypeState.actresses, showlist))

```

```python eval
docdemo_from(ActressType, MultiDataTypeState, component=actresses_example)
```

Setting the type of `actresses` to be `actresses: list[dict[str,str]]` would fail as it cannot be understood that the `value` for the `pages key` is actually a `list`.




## Combine Multiple Var Operations

You can also combine multiple var operations together, as seen in the next example.

```python exec
import random

class VarNumberState(State):
    number: int

    def update(self):
        self.number = random.randint(0, 100)

def var_number_example():
    return rx.vstack(
        rx.heading(f"The number is {VarNumberState.number}", size="lg"),
        # Var operations can be composed for more complex expressions.
        rx.cond(
            VarNumberState.number % 2 == 0,
            rx.text("Even", color="green"),
            rx.text("Odd", color="red"),
        ),
        rx.button("Update", on_click=VarNumberState.update),
    )
```

```python eval
docdemo_from(VarNumberState, component=var_number_example, imports=["import random"])
```

We could have made a computed var that returns the parity of `number`, but
it can be simpler just to use a var operation instead.

Var operations may be generally chained to make compound expressions, however
some complex transformations not supported by var operations must use computed vars
to calculate the value on the backend.