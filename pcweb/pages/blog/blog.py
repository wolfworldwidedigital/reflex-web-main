import reflex as rx
import flexdown

from pcweb import styles
from pcweb.styles import text_colors as tc
from pcweb.styles import colors as c
from pcweb.templates.webpage import webpage
from pcweb.flexdown import component_map

PAGES_PATH = "blog/"


def get_blog_data(paths):
    blogs = {}
    for path in reversed(sorted(paths)):
        document = flexdown.parse_file(path)
        path = path.replace(".md", "")
        blogs[path] = document
    return blogs


def get_route(path: str):
    """Get the route for a page."""
    return path.replace(PAGES_PATH, "").replace(".md", "")


def page(document) -> rx.Component:
    """Create a page."""
    meta = document.metadata
    return rx.container(
        rx.heading(meta["title"], mt=12, mb=4, font_weight="semibold"),
        rx.hstack(
            rx.avatar(name=meta["author"], size="xs"),
            rx.text(meta["author"], font_size="0.9rem"),
            rx.text(" · "),
            rx.text(str(meta["date"]), font_size="0.9rem"),
        ),
        rx.image(
            src=f"{meta['image']}",
            object_fit="contain",
            shadow="sm",
            my=8,
            border_radius="8px",
        ),
        flexdown.render(document, component_map=component_map),
        padding_bottom="8em",
    )


paths = flexdown.utils.get_flexdown_files(PAGES_PATH)
blogs = get_blog_data(paths)


class Gallery(rx.Model):
    name: str
    date: str
    tags: list[str]
    description: str
    img: str
    gif: str
    url: str
    source: str


def component_grid():
    posts = []
    for path, document in blogs.items():
        meta = document.metadata
        posts.append(
            rx.link(
                rx.box(
                    height="10rem",
                    background_image=meta["image"],
                    background_size="cover",
                    background_position="center",
                    background_repeat="no-repeat",
                    w="100%",
                ),
                rx.box(
                    rx.heading(
                        meta["title"],
                        font_size="1.2rem",
                        mb="0.5em",
                    ),
                    rx.text(
                        meta["description"],
                        font_size="0.8rem",
                    ),
                    rx.divider(),
                    rx.spacer(),
                    rx.hstack(
                        rx.vstack(
                            rx.text("Written by", font_size="0.6rem"),
                            rx.hstack(
                                rx.avatar(
                                    name=meta["author"],
                                    size="sm",
                                    bg=c["indigo"][800],
                                    color="#DACEEE",
                                ),
                                rx.text(meta["author"], font_size="0.8rem"),
                            ),
                            align_items="left",
                        ),
                        rx.spacer(),
                        rx.vstack(
                            rx.text("Published on", font_size="0.6rem"),
                            rx.text(str(meta["date"]), font_size="0.8em"),
                            align_items="left",
                        ),
                        color=tc["docs"]["body"],
                        padding_bottom="0.5em",
                        width="100%",
                    ),
                    p=4,
                    height="100%",
                    width="100%",
                ),
                border="1px solid #eee",
                border_radius="8px",
                overflow="hidden",
                bg_color="white",
                _hover={
                    "box_shadow": "0px 0px 0px 1px rgba(52, 46, 92, 0.12), 0px 2px 3px rgba(3, 3, 11, 0.1), 0px 12px 8px rgba(3, 3, 11, 0.04), 0px 8px 12px -4px rgba(3, 3, 11, 0.02)"
                },
                href=path,
            ),
        )
    return rx.box(
        rx.responsive_grid(*posts, columns=[1, 2, 2, 2, 3], gap=4),
    )


@webpage(path="/blog", title="Blog")
def blg():
    return rx.container(
        rx.vstack(
            rx.box(
                rx.heading("Reflex Blog", font_size=styles.H1_FONT_SIZE, mt=12, mb=4),
                rx.text(
                    "The latest news from the Reflex team. ",
                    color=tc["docs"]["body"],
                ),
                rx.divider(),
                text_align="left",
                width="100%",
            ),
            component_grid(),
            align_items="stretch",
            min_height="80vh",
            margin_bottom="4em",
            padding_y="2em",
        ),
        flex_direction="column",
        max_width="960px",
    )


@webpage(path="/blog/2023-08-02-seed-annoucement", title="Seed Annoucement")
def seed():
    return page(blogs["blog/2023-08-02-seed-annoucement"])


@webpage(path="/blog/2023-06-28-rebrand-to-reflex", title="Rebrand to Reflex")
def rebrand():
    return page(blogs["blog/2023-06-28-rebrand-to-reflex"])


@webpage(
    path="/blog/2023-09-28-unlocking-new-workflows-with-background-tasks",
    title="Unlocking New Workflows with Background Tasks",
)
def background_tasks():
    return page(blogs["blog/2023-09-28-unlocking-new-workflows-with-background-tasks"])


@webpage(path="/blog/2023-10-11-graphing-update", title="Graphing Update")
def graphing_update():
    return page(blogs["blog/2023-10-11-graphing-update"])


@webpage(
    path="/blog/2023-10-25-implementing-sign-in-with-google",
    title="Implementing Sign In with Google",
)
def sign_in_with_google():
    return page(blogs["blog/2023-10-25-implementing-sign-in-with-google"])
