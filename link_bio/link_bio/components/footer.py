import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size 
from link_bio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"© 2014-{datetime.date.today().year} celikadev by Alba Muñoz v3.", 
            href="https://www.linkedin.com/in/alba-munoz-rodriguez/",
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM MADRID TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
            ),
        margin_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value
    )