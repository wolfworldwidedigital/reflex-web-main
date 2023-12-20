```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo
```

A primitive useful for grid layouts. Grid is Box with display, grid and it comes with helpful style shorthand. It renders a div element.

```python eval
docdemo("""rx.grid(
    rx.grid_item(row_span=1, col_span=1, bg="lightgreen"),
    rx.grid_item(row_span=1, col_span=1, bg="lightblue"),
    rx.grid_item(row_span=1, col_span=1, bg="purple"),
    rx.grid_item(row_span=1, col_span=1, bg="orange"),
    rx.grid_item(row_span=1, col_span=1, bg="yellow"),
    template_columns="repeat(5, 1fr)",
    h="10em",
    width="100%",
    gap=4,
)""")
```

In some layouts, you may need certain grid items to span specific amount of columns or rows instead of an even distribution. To achieve this, you need to pass the col_span prop to the GridItem component to span across columns and also pass the row_span component to span across rows. You also need to specify the template_columns and template_rows.

```python eval
docdemo("""rx.grid(
    rx.grid_item(row_span=2, col_span=1, bg="lightblue"),
    rx.grid_item(col_span=2, bg="lightgreen"),
    rx.grid_item(col_span=2, bg="yellow"),
    rx.grid_item(col_span=4, bg="orange"),
    template_rows="repeat(2, 1fr)",
    template_columns="repeat(5, 1fr)",
    h="200px",
    width="100%",
    gap=4,
)""")
```

