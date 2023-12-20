```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo
```

Containers are used to constrain a content's width to the current breakpoint, while keeping it fluid.

```python eval
docdemo("""rx.container(
    rx.box("Example", bg="blue", color="white", width="50%"),
    center_content=True,
    bg="lightblue",
)""")
```
