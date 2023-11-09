import reflex as rx
from link_bio.components.link_icon import link_icon 
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size 
from link_bio.styles.colors import TextColor as TextColor
import datetime

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Alba Muñoz", size="xl"),
            rx.vstack(
                rx.heading(
                    "Alba Muñoz", 
                    size="lg",
                    color=TextColor.HEADER.value
                ),
                rx.text(
                    "@alba.mur",
                    margin_top=Size.ZERO.value ,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon("https://www.linkedin.com/in/alba-munoz-rodriguez/"),
                    link_icon("https://www.linkedin.com/in/alba-munoz-rodriguez/"),
                    link_icon("https://www.linkedin.com/in/alba-munoz-rodriguez/"),
                ),
                align_items="start",
                spacing=Size.DEFAULT.value
            )
        ),
        rx.flex(
            rx.spacer(),
            info_text(
                f"{experience()}",
                "año de experiencia"
            ),
            rx.spacer(),
            info_text(
                "+1",
                "aplicaciones creadas"
            ),
            rx.spacer(),
            width="100%"
        ),
        rx.text(
            f"""
            Soy desarrolladora web desde hace más de {experience()} año. 
            Actualmente trabajo como desarrolladora de software dedicado a 
            la automatización de tareas. Además creo aplicaciones full-stack 
            como práctica de los conocimientos que sigo adquiriendo día a día. 
            Aquí podrás encontrar todos mis enlaces de interés. ¡Bienvenid@!
            """,
            color=TextColor.BODY.value
            ),
        spacing=Size.BIG.value,
        align_items="start"
    )


def experience() -> int:
    return datetime.date.today().year - 2022