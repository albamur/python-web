import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size 

def links() -> rx.Component:
    return rx.vstack(
        title("Links de interés"),
        link_button(
            "Linkedin",
            "Revisa mi experiencia",
            "https://www.linkedin.com/in/alba-munoz-rodriguez/"
            ),
        link_button(
            "Instagram",
            "Visita mi instagram", 
            "https://www.linkedin.com/in/alba-munoz-rodriguez/"
            ),
        link_button(
            "Discord", 
            "Contacta conmigo", 
            f"mail to:"
            ),
        title("Links de interés"),
        link_button(
            "Linkedin",
            "Revisa mi experiencia",
            "https://www.linkedin.com/in/alba-munoz-rodriguez/"
            ),
        width="100%",
        spacing=Size.MEDIUM.value
    )