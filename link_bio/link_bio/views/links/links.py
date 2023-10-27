import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Linkedin","Revisa mi experiencia", "https://www.linkedin.com/in/alba-munoz-rodriguez/"),
        link_button("Instagram","Visita mi instagram", "https://www.linkedin.com/in/alba-munoz-rodriguez/"),
        link_button("Discord", "Contacta conmigo", "https://www.linkedin.com/in/alba-munoz-rodriguez/"),
        width="100%",
    )