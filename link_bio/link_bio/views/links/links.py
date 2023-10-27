import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Linkedin", "https://www.linkedin.com/in/alba-munoz-rodriguez/"),
        link_button("Instagram", "https://www.linkedin.com/in/alba-munoz-rodriguez/"),
        link_button("Discord", "https://www.linkedin.com/in/alba-munoz-rodriguez/")
    )