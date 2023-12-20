import reflex as rx

from pcweb.templates.docpage import (
    doccode,
    docheader,
    docpage,
    doctext,
    subheader,
)

code_example1 = """rx.text('hello world', color='blue')"""


@docpage()
def navbar():
    return rx.box(
        docheader("Navigation Bar", first=True),
        doctext(
            "A navigation bar, also known as a navbar, is a common UI element found at the top of a webpage or application. It typically provides links or buttons to the main sections of a website or application, allowing users to easily navigate and access the different pages. ",
        ),
        doctext(
            "Navigation bars are useful for web apps because they provide a consistent and intuitive way for users to navigate through the app. ",
            "Having a clear and consistent navigation structure can greatly improve the user experience by making it easy for users to find the information they need and access the different features of the app. ",
        ),
        subheader("Recipe"),
        doctext(
            "In this recipe, we will create a navbar component that can be used to create a navigation bar for a web app. ",
            "The navbar will be a simple horizontal bar that contains a logo and a list of links to the different pages of the app. ",
        ),
        doctext(
            "In this example we want the navbar to stick to the top of the page, so we will use the ",
            rx.code('position= "fixed"'),
            " prop to make the navbar fixed to the top of the page. ",
            "We will also use the ",
            rx.code("top= 0"),
            " and ",
            rx.code('z_index="1'),
            " props to make sure the navbar is always on top of the screen and above the other components on the page. ",
        ),
        doccode(
            """
            import reflex as rx

            def navbar():
                return rx.box(
                    rx.hstack(
                        rx.image(src="favicon.ico"),
                        rx.heading("My App")
                    ),
                    rx.spacer(),
                    rx.menu(
                        rx.menu_button("Menu"),
                    ),
                    position="fixed",
                    width="100%",
                    top="0px",
                    z_index="5"
                )
            """
        ),
    )
