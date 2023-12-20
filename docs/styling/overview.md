```python exec
from pcweb.templates.docpage import docdemo, doclink
from pcweb.base_state import State
import reflex as rx
import inspect
from pcweb.pages.docs.styling import custom_stylesheets
```

# Styling 

Reflex components can be styled using the full power of [CSS]({"https://www.w3schools.com/css/"}).

There are three main ways to add style to your app and they take precedence in the following order:
1. **Inline:** Styles applied to a single component instance.
2. **Component:** Styles applied to components of a specific type.
3. **Global:** Styles applied to all components.

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Style keys can be any valid CSS property name."),
        rx.alert_description(
            "To be consistent with Python standards, you can specify keys in ",
            rx.code("snake_case"),
            ".",
        ),
    ),
    status="success",
)
```

## Global Styles

You can pass a style dictionary to your app to apply base styles to all components.

For example, you can set the default font family and font size for your app here just once rather than having to set it on every component.

```python
style = {
    "font_family": "Comic Sans MS",
    "font_size": "16px",
}

app = rx.App(style=style)
```

## Component Styles

In your style dictionary, you can also specify default styles for specific component types or arbitrary CSS classes and IDs.

```python
accent_color = "#f81ce5"
style = {
    "::selection": {
        "background_color": accent_color,
    },
    ".some-css-class": {
        "text_decoration": "underline",
    },
    "#special-input": \{"width": "20vw"},
    rx.Text: {
        "font_family": styles.SANS,
    },
    rx.Divider: {
        "margin_bottom": "1em",
        "margin_top": "0.5em",
    },
    rx.Heading: {
        "font_weight": "500",
    },
    rx.Code: {
        "color": accent_color,
    },
}

app = rx.App(style=style)
```

Using style dictionaries like this, you can easily create a consistent theme for your app.

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Note the use of the uppercase component names."),
        rx.alert_description(
            "We specify the component classes as keys, rather than their constructors. ",
        ),
    ),
    status="warning",
)
```

```python eval
rx.box(height=2)
```

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Watch out for underscores in class names and IDs"),
        rx.alert_description(
            "Reflex automatically converts ",
            rx.code("snake_case"),
            " identifiers into ",
            rx.code("camelCase"),
            " format when applying styles. To ensure consistency, it is recommended to use the dash character "
            "or camelCase identifiers in your own class names and IDs. ",
            "To style third-party libraries relying on underscore class names, an external stylesheet should be "
            "used. See ",
            doclink("custom stylesheets", href=custom_stylesheets.path),
            " for how to reference external CSS files.",
        ),
    ),
    status="warning",
)
```

## Inline Styles

Inline styles apply to a single component instance. They are passed in as regular props to the component.

```python demo
rx.text(
    "Hello World",
    background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
    background_clip="text",
    font_weight="bold",
    font_size="2em",
)
```

Children components inherit inline styles unless they are overridden by their own inline styles.

```python demo
rx.box(
    rx.hstack(
        rx.button("Default Button"),
        rx.button("Red Button", color="red"),
    ),
    color="blue",
)
```

## Tailwind

Reflex supports [Tailwind CSS]({"https://tailwindcss.com/"}) out of the box. To enable it, pass in a dictionary for the `tailwind` argument of your `rxconfig.py`:

```python
import reflex as rx


class AppConfig(rx.Config):
    pass


config = AppConfig(
    app_name="app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    tailwind=\{},
)
```

All Tailwind configuration options are supported. Plugins and presets are automatically wrapped in `require()`:

```python
config = AppConfig(
    app_name="app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    tailwind={
        "theme": {
            "extend": \{},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)
```

You can use any of the [utility classes]({"https://tailwindcss.com/docs/utility-first"}) under the `class_name` prop:

```python demo
rx.box(
    "Hello World",
    class_name="text-4xl text-center text-blue-500",
)
```

## Disabling Tailwind

If you want to disable Tailwind in your configuration, you can do so by setting the `tailwind` config to `None`. This can be useful if you need to temporarily turn off Tailwind for your project:

```python
config = rx.Config(app_name="app", tailwind=None)
```

With this configuration, Tailwind will be disabled, and no Tailwind styles will be applied to your application.


## Special Styles

We support all of Chakra UI's [pseudo styles]({"https://chakra-ui.com/docs/features/style-props#pseudo"}).

Below is an example of text that changes color when you hover over it.

```python demo
rx.box(
    rx.text("Hover Me", _hover={"color": "red"}),
)
```


## Style Prop

Inline styles can also be set with a `style` prop. This is useful for reusing styles betweeen multiple components.

```python exec
text_style = {
    "color": "green",
    "font_family": "Comic Sans MS",
    "font_size": "1.2em",
    "font_weight": "bold",
    "box_shadow": "rgba(240, 46, 170, 0.4) 5px 5px, rgba(240, 46, 170, 0.3) 10px 10px",
}
```

```python
text_style={text_style}
```

```python demo
rx.vstack(
    rx.text("Hello", style=text_style),
    rx.text("World", style=text_style),
)
```

```python exec
style1 = {
    "color": "green",
    "font_family": "Comic Sans MS",
    "border_radius": "10px",
    "background_color": "rgb(107,99,246)",
}
style2 = {
    "color": "white",
    "border": "5px solid #EE756A",
    "padding": "10px",
}
```

```python
style1={style1}
style2={style2}
```

```python demo
rx.box(
    "Multiple Styles",
    style=[style1, style2],
)
```

The style dictionaries are applied in the order they are passed in. This means that styles defined later will override styles defined earlier.

