import reflex as rx

from pcweb.templates.docpage import doccode, docheader, docpage, doctext, subheader

from pcweb.base_state import State


code_example = """
import reflex as rx
from typing import List, Dict

RAW_DATA = [
    {"name": "Alice", "tags": "tag1"},
    {"name": "Bob", "tags": "tag2"},
    {"name": "Charlie", "tags": "tag1"},
]
RAW_DATA_COLUMNS = ["Name", "tags"]


class FilteredTableState(rx.State):
    filter_expr: str = ""
    data: Dict[str, Dict[str, str]] = RAW_DATA

    @rx.cached_var
    def filtered_data(self) -> List[Dict[str, str]]:
        # Use this generated filtered data view in the `rx.foreach` of
        #  the table renderer of rows
        # It is dependent on `filter_expr`
        # This `filter_expr` is set by an rx.input
        return [
            row
            for row in self.data
            if self.filter_expr == ""
            or self.filter_expr != ""
            and self.filter_expr == row["tags"]
        ]

    def input_filter_on_change(self, value):
        self.filter_expr = value
        # for DEBUGGING
        yield rx.console_log(f"Filter set to: {self.filter_expr}")


def render_row(row):
    return rx.tr(rx.td(row["name"]), rx.td(row["tags"]))


def render_rows():
    return [
        rx.foreach(
            # use data filtered by `filter_expr` as update by rx.input
            FilteredTableState.filtered_data,
            render_row,
        )
    ]


def render_table():
    return rx.table_container(
        rx.table(
            rx.thead(rx.tr(*[rx.th(column) for column in RAW_DATA_COLUMNS])),
            rx.tbody(*render_rows()),
        )
    )


def index() -> rx.Component:
    return rx.box(
        rx.box(
            rx.heading(
                "Filter by tags:",
                size="sm",
            ),
            rx.input(
                on_change=FilteredTableState.input_filter_on_change,
                value=FilteredTableState.filter_expr,
                debounce_timeout=1000,
            ),
        ),
        rx.box(
            render_table(),
        ),
    )


app = rx.App()
app.add_page(index, route="/")
app.compile()
"""


@docpage()
def filtered_table():
    return rx.box(
        docheader("Table with row filtering", first=True),
        doctext("A Table that you can apply a simple row selection filtering by tag"),
        subheader("Recipe"),
        rx.center(rx.image(src="/gallery/filtered_table.gif")),
        doctext(
            "This recipe uses a ",
            rx.code("rx.foreach"),
            " for the row generation with a computed var filtering the data for rows",
            " using an input value for filter value",
        ),
        doctext(
            "Additionally, the filter input uses a debounce that limits the ",
            "update,  prevents filtered data to be calculated on every keypress.",
        ),
        doccode(code_example),
    )
