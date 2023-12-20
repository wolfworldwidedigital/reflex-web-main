```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo, docdemobox


basic_button_group = (
"""rx.button_group(
            rx.button('Option 1'),
            rx.button('Option 2'),
            rx.button('Option 3'),
        )
"""
)

button_group_attached = (
"""rx.button_group(
            rx.button('Option 1'),
            rx.button('Option 2'),
            rx.button('Option 3'),
            is_attached=True,
        )

"""  
)

button_group_variant = (
"""rx.button_group(
            rx.button('Option 1'),
            rx.button('Option 2'),
            rx.button('Option 3'),
            variant='ghost',
        )

"""  
)

button_group_sizes = (
"""rx.button_group(
            rx.button('Large Button', size='lg'),
            rx.button('Medium Button', size='md'),
            rx.button('Small Button', size='sm'),
        )

"""  
)

button_group_disable = (
"""rx.button_group(
            rx.button('Option 1'),
            rx.button('Option 2'),
            rx.button('Option 3'),
            is_disabled=True,
        )

"""  
)

button_group_spacing = (
"""rx.button_group(
            rx.button('Option 1'),
            rx.button('Option 2'),
            rx.button('Option 3'),
            spacing=8,
        )

"""  

)
```

The `rx.button_group` component allows you to create a group of buttons that are visually connected and styled together.
This is commonly used to group related actions or options in your application's user interface.

## Basic Usage

Here's an example of how to use the `rx.button_group` component to create a simple group of buttons:

```python eval
docdemo(basic_button_group)
```

In this example, a button group is created with three buttons. The buttons are visually connected, and there 
is a default spacing of `2` pixels between them.

## Adjusting ButtonGroup Properties

You can customize the appearance and behavior of the `rx.button_group` component by adjusting
its properties. For instance, you can set `is_attached` prop to `True` to make the buttons 
appear flushed together:

```python eval
docdemo(button_group_attached)
```
In this example, the `is_attached` property is set to `True`, resulting in the buttons having a seamless appearance.

## ButtonGroup Variants

Just like the `button` component, you can customize the visual style of your buttons using the `variant` prop. 
This will apply to all buttons in the group.

```python eval
docdemo(button_group_variant)
```
In this example, the `variant` prop is set to `ghost`, applying the variant style to all buttons in the group.

## ButtonGroup Sizes

Similarly, you can adjust the size of buttons within a button group using the `size` prop. 
This prop allows you to choose from different size options, affecting all buttons within the group.

```python eval
docdemo(button_group_sizes)
```
In this example, the `size` prop is used to set the size of all buttons within the group, with options such as `"lg"` (large), `"md"` (medium), and `"sm"` (small).

## Disabling ButtonGroup

You can also disable all the buttons within a button group by setting the `is_disabled` prop to `True`:

```python eval
docdemo(button_group_disable)
```
In this case, all the buttons within the group will be disabled and unclickable.

## Customizing Spacing

The `spacing` prop allows you to control the gap between buttons within the group. Here's an example of setting a custom spacing of `8` pixels:

```python eval
docdemo(button_group_spacing)
```
By setting `spacing` to `8`, the buttons will have a larger gap between them.

```python eval
rx.alert(
    rx.unordered_list(
        rx.list_item("You can nest other components or elements within the button group to create more complex layouts."),
        rx.list_item("Button groups are a useful way to visually organize related actions or options in your application, providing a consistent and cohesive user interface."),
        rx.list_item("Experiment with different combinations of props to achieve the desired styling and behavior for your button groups in Reflex-based applications."),
    ),
    icon=True,
)
```