import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.text("Hola Reflex", color="blue")

def about():
    return rx.text('About Page')

app = rx.App()
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.compile()