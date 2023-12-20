```python exec
from pcweb.templates.docpage import doccode, docdemo
import reflex as rx
from pcweb.pages.docs.tutorial.final_app import ChatappState
from pcweb.pages.docs.tutorial import style
import inspect
```

# Final App

We will use OpenAI's API to give our chatbot some intelligence.

## Using the API

We need to modify our event handler to send a request to the API.

```python exec
def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(rx.text(question, style=style.question_style), text_align="right"),
        rx.box(rx.text(answer, style=style.answer_style), text_align="left"),
        margin_y="1em",
        width="100%",
    )


def chat1() -> rx.Component:
    return rx.box(
        rx.foreach(
            ChatappState.chat_history, lambda messages: qa(messages[0], messages[1])
        )
    )


def show_code_using_the_api():
    # state.py
    import os
    from openai import OpenAI

    openai.api_key = os.environ["OPENAI_API_KEY"]

    ...

    def answer(self):
        # Our chatbot has some brains now!
        client = OpenAI()
        session = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds.
        answer = ""
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    # presence of 'None' indicates the end of the response
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.chat_history[-1][0], answer)
                yield



def action_bar3() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=ChatappState.question,
            placeholder="Ask a question",
            on_change=ChatappState.set_question,
            style=style.input_style,
        ),
        rx.button("Ask", on_click=ChatappState.answer4, style=style.button_style),
    )


def rendered_code_using_the_api():
    return rx.container(
        chat1(),
        action_bar3(),
    )

```

```python eval
docdemo(
    inspect.getsource(show_code_using_the_api).replace("def show_code_using_the_api():", ""),
    comp=rendered_code_using_the_api()
)
```

Finally, we have our chatbot!

## Final Code

We wrote all our code in three files, which you can find below.


```python exec
def show_final_code():
    # chatapp.py
    import reflex as rx

    from chatapp import style
    from chatapp.state import State


    def qa(question: str, answer: str) -> rx.Component:
        return rx.box(
            rx.box(rx.text(question, text_align="right"), style=style.question_style),
            rx.box(rx.text(answer, text_align="left"), style=style.answer_style),
            margin_y="1em",
        )

    def chat() -> rx.Component:
        return rx.box(
            rx.foreach(
                State.chat_history,
                lambda messages: qa(messages[0], messages[1])
            )
        )


    def action_bar() -> rx.Component:
        return rx.hstack(
            rx.input(
                value=State.question,
                placeholder="Ask a question",
                on_change=State.set_question,
                style=style.input_style,
            ),
            rx.button("Ask", on_click=State.answer, style=style.button_style),
        )


    def index() -> rx.Component:
        return rx.container(
            chat(),
            action_bar(),
        )


    app = rx.App()
    app.add_page(index)
    app.compile()


def show_final_state():
    # state.py
    import reflex as rx
    import os
    import openai


    openai.api_key = os.environ["OPENAI_API_KEY"]

    class State(rx.State):

        # The current question being asked.
        question: str

        # Keep track of the chat history as a list of (question, answer) tuples.
        chat_history: list[tuple[str, str]]

        def answer(self):
            # Our chatbot has some brains now!
            client = OpenAI()
            session = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": self.question}
                ],
                stop=None,
                temperature=0.7,
                stream=True,
            )

            # Add to the answer as the chatbot responds.
            answer = ""
            self.chat_history.append((self.question, answer))

            # Clear the question input.
            self.question = ""
            # Yield here to clear the frontend input before continuing.
            yield

            for item in session:
                if hasattr(item.choices[0].delta, "content"):
                    if item.choices[0].delta.content is None:
                        # presence of 'None' indicates the end of the response
                        break
                    answer += item.choices[0].delta.content
                    self.chat_history[-1] = (self.chat_history[-1][0], answer)
                    yield


def show_final_style():
    # style.py

    # Common styles for questions and answers.
    shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
    chat_margin = "20%"
    message_style = dict(
        padding="1em",
        border_radius="5px",
        margin_y="0.5em",
        box_shadow=shadow,
    )

    # Set specific styles for questions and answers.
    question_style = message_style | dict(bg="#F5EFFE", margin_left=chat_margin)
    answer_style = message_style | dict(bg="#DEEAFD", margin_right=chat_margin)

    # Styles for the action bar.
    input_style = dict(
        border_width="1px", padding="1em", box_shadow=shadow
    )
    button_style = dict(
        bg="#CEFFEE", box_shadow=shadow
    )
```

```python eval
doccode(inspect.getsource(show_final_code).replace("def show_final_code():", ""))
```

```python eval
doccode(inspect.getsource(show_final_state).replace("def show_final_state():", ""))
```

```python eval
doccode(inspect.getsource(show_final_style).replace("def show_final_style():", ""))
```

## Next Steps

Congratulations! You have built your first chatbot. From here, you can read through the rest of the documentations to learn about Reflex in more detail. The best way to learn is to build something, so try to build your own app using this as a starting point!


