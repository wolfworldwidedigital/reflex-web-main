```python exec
import reflex as rx
from pcweb.base_state import State
from pcweb.templates.docpage import docdemo, docdemobox


basic_button = """rx.button("Click Me!")
"""
button_style = """rx.button_group(
    rx.button("Example", bg="lightblue", color="black", size = 'sm'),
    rx.button("Example", bg="orange", color="white", size = 'md'),
    rx.button("Example", color_scheme="red", size = 'lg'),
    space = "1em",
)
"""
button_visual_states = """rx.button_group(
    rx.button("Example", bg="lightgreen", color="black", is_loading = True),
    rx.button("Example", bg="lightgreen", color="black", is_disabled = True),
    rx.button("Example", bg="lightgreen", color="black", is_active = True),
    space = '1em',
)
"""

button_group_example = """rx.button_group(
    rx.button(rx.icon(tag="minus"), color_scheme="red"),
    rx.button(rx.icon(tag="add"), color_scheme="green"),
    is_attached=True,
)
"""

button_state = """class ButtonState(State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1
"""
exec(button_state)
button_state_example = """rx.hstack(
    rx.button(
        "Decrement",
        bg="#fef2f2",
        color="#b91c1c",
        border_radius="lg",
        on_click=ButtonState.decrement,
    ),
    rx.heading(ButtonState.count, font_size="2em", padding_x="0.5em"),
    rx.button(
        "Increment",
        bg="#ecfdf5",
        color="#047857",
        border_radius="lg",
        on_click=ButtonState.increment,
    ),
)
"""


button_state_code = f"""
import reflex as rx

{button_state.replace("(State)", "(rx.State)")}

def index():
    return {button_state_example}

app = rx.App()
app.add_page(index)
app.compile()"""

button_state2 = """class ExampleButtonState(State):
    text_value: str = "Random value"
"""
exec(button_state2)

button_state2_render_code = """rx.vstack(
	rx.text(ExampleButtonState.text_value),
        rx.button(
            "Change Value",
            on_click=ExampleButtonState.set_text_value("Modified value"))
    )
"""

button_state2_code = f"""
import reflex as rx

{button_state2.replace("(State)", "(rx.State)")}

def index():
    return {button_state2_render_code}

app = rx.App()
app.add_page(index)
app.compile()"""


button_sizes = (
"""rx.button_group(
        rx.button(
        'Example', bg='lightblue', color='black', size='sm'
        ),
        rx.button(
            'Example', bg='orange', color='white', size='md'
        ),
        rx.button('Example', color_scheme='red', size='lg'),
)
"""  
)

button_colors = (
"""rx.button_group(
        rx.button('White Alpha', color_scheme='whiteAlpha', min_width='unset'),
        rx.button('Black Alpha', color_scheme='blackAlpha', min_width='unset'),
        rx.button('Gray', color_scheme='gray', min_width='unset'),
        rx.button('Red', color_scheme='red', min_width='unset'),
        rx.button('Orange', color_scheme='orange', min_width='unset'),
        rx.button('Yellow', color_scheme='yellow', min_width='unset'),
        rx.button('Green', color_scheme='green', min_width='unset'),
        rx.button('Teal', color_scheme='teal', min_width='unset'),
        rx.button('Blue', color_scheme='blue', min_width='unset'),
        rx.button('Cyan', color_scheme='cyan', min_width='unset'),
        rx.button('Purple', color_scheme='purple', min_width='unset'),
        rx.button('Pink', color_scheme='pink', min_width='unset'),
        rx.button('LinkedIn', color_scheme='linkedin', min_width='unset'),
        rx.button('Facebook', color_scheme='facebook', min_width='unset'),
        rx.button('Messenger', color_scheme='messenger', min_width='unset'),
        rx.button('WhatsApp', color_scheme='whatsapp', min_width='unset'),
        rx.button('Twitter', color_scheme='twitter', min_width='unset'),
        rx.button('Telegram', color_scheme='telegram', min_width='unset'),
        width='100%',
)

""" 
)

button_colors_render_code = (
"""rx.button_group(
        rx.button('White Alpha', color_scheme='whiteAlpha'),
        rx.button('Black Alpha', color_scheme='blackAlpha'),
        rx.button('Gray', color_scheme='gray'),
        rx.button('Red', color_scheme='red'),
        rx.button('Orange', color_scheme='orange'),
        rx.button('Yellow', color_scheme='yellow'),
        rx.button('Green', color_scheme='green'),
        rx.button('Teal', color_scheme='teal'),
        rx.button('Blue', color_scheme='blue'),
        rx.button('Cyan', color_scheme='cyan'),
        rx.button('Purple', color_scheme='purple'),
        rx.button('Pink', color_scheme='pink'),
        rx.button('LinkedIn', color_scheme='linkedin'),
        rx.button('Facebook', color_scheme='facebook'),
        rx.button('Messenger', color_scheme='messenger'),
        rx.button('WhatsApp', color_scheme='whatsapp'),
        rx.button('Twitter', color_scheme='twitter'),
        rx.button('Telegram', color_scheme='telegram'),
)

""" 
)

button_variants = (
"""rx.button_group(
        rx.button('Ghost Button', variant='ghost'),
        rx.button('Outline Button', variant='outline'),
        rx.button('Solid Button', variant='solid'),
        rx.button('Link Button', variant='link'),
        rx.button('Unstyled Button', variant='unstyled'),
    )
"""  

)

button_disable = (
"""rx.button('Inactive button', is_disabled=True)"""  
)
  
loading_states = (
"""rx.button(
            'Random button',
            is_loading=True,
            loading_text='Loading...',
            spinner_placement='start'
    )
"""  
)

stack_buttons_vertical = (
"""rx.stack(
        rx.button('Button 1'),
        rx.button('Button 2'),
        rx.button('Button 3'),
        direction='column',
)

"""  
)

stack_buttons_horizontal = (
"""rx.stack(
        rx.button('Button 1'),
        rx.button('Button 2'),
        rx.button('Button 3'),
        direction='row',
)
"""  
)

button_group = (
"""rx.button_group(
            rx.button('Option 1'),
            rx.button('Option 2'),
            rx.button('Option 3'),
            variant='outline',
	        is_attached=True,
        )
"""  

)

```

Buttons are essential elements in your application's user interface that users can click to trigger events. 
This documentation will help you understand how to use button components effectively in your Reflex application.

## Basic Usage
A basic button component is created using the `rx.button` method:

```python eval
docdemo(basic_button)
```
## Button Sizing
You can change the size of a button by setting the size prop to one of the following 
values: `xs`,`sm`,`md`, or `lg`.

```python eval
docdemo(button_sizes)
```

## Button colors
Customize the appearance of buttons by adjusting their color scheme through the color_scheme prop. 
You have the flexibility to choose from a range of color scales provided by your design 
system, such as whiteAlpha, blackAlpha, gray, red, blue, or even utilize your own custom color scale.

```python eval
docdemobox(
    eval(button_colors)
)
```

```python
{button_colors_render_code.strip()}
```

## Button Variants
You can customize the visual style of your buttons using the variant prop. Here are the available button variants:
- `ghost`: A button with a transparent background and visible text.
- `outline`: A button with no background color but with a border.
- `solid`: The default button style with a solid background color.
- `link`: A button that resembles a text link.
- `unstyled`: A button with no specific styling.

```python eval
docdemo(button_variants)
```
## Disabling Buttons
Make buttons inactive by setting the `is_disabled` prop to `True`.

```python eval
docdemo(button_disable)
```

## Handling Loading States
To indicate a loading state for a button after it's clicked, you can use the following properties:
- `is_loading`: Set this property to `True` to display a loading spinner.
- `loading_text`: Optionally, you can provide loading text to display alongside the spinner.
- `spinner_placement`: You can specify the placement of the spinner element, which is 'start' by default.


```python eval
docdemo(loading_states)
```

## Handling Click Events
You can define what happens when a button is clicked using the `on_click` event argument. 
For example, to change a value in your application state when a button is clicked:

```python eval
docdemobox(
    eval(button_state2_render_code)
)
```

```python
{button_state2_code.strip()}
```

In the code above, The value of `text_value` is changed through the `set_text_value` event handler upon clicking the button. 
Reflex provides a default setter event_handler for every base var which can be accessed by prefixing the base var with the `set_` keyword.

Here’s another example that creates two buttons to increase and decrease a count value:

```python eval
docdemobox(
    eval(button_state_example)
)
```

```python
{button_state_code.strip()}
```

In this example, we have a `ButtonState` state class that maintains a count base var. 
When the "Increment" button is clicked, it triggers the `ButtonState.increment` event handler, and when the "Decrement" 
button is clicked, it triggers the `ButtonState.decrement` event handler.

## Special Events and Server-Side Actions

Buttons in Reflex can trigger special events and server-side actions,
allowing you to create dynamic and interactive user experiences.
You can bind these events to buttons using the `on_click` prop.
For a comprehensive list of 
available special events and server-side actions, please refer to the
[Special Events Documentation](/docs/api-reference/special-events) for detailed information and usage examples.

## Grouping Buttons
In your Reflex application, you can group buttons effectively using the `Stack` component and 
the `ButtonGroup` component. Each of these options offers unique capabilities to help you structure 
and style your buttons.

## Using the `Stack` Component
The `Stack` component allows you to stack buttons both vertically and horizontally, providing a flexible
layout for your button arrangements.

## Stack Buttons Vertically:

```python eval
docdemo(stack_buttons_vertical)
```

## Stack Buttons Horizontally:

```python eval
docdemo(stack_buttons_horizontal)
```
With the `stack` component, you can easily create both vertical and horizontal button arrangements.

## Using the `rx.button_group` Component
The `ButtonGroup` component is designed specifically for grouping buttons. It allows you to:
- Set the `size` and `variant` of all buttons within it.
- Add `spacing` between the buttons.
- Flush the buttons together by removing the border radius of their children as needed.

```python eval
docdemo(button_group)
```
```python eval
rx.alert(
    icon=True,
    title=rx.text(
        "The ",
        rx.code("button_group"),
        " component stacks buttons horizontally, whereas the ",
        rx.code("stack"),
        " component allows stacking buttons both vertically and horizontally.",
    ),
)
```

