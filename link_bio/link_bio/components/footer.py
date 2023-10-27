import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"© 2014-{datetime.date.today().year} celiakdev BY ALBA MUÑOZ V3.", 
            href="https://www.linkedin.com/in/alba-munoz-rodriguez/"
        ),
        rx.text("BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.")
    )