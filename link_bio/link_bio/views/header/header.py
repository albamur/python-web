import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Alba Muñoz", size="xl"),
        rx.text("@alba.mur"),
        rx.text("Hola mi nombre es Alba Muñoz"),
        rx.text("""Soy ingeniero de software desde hace más de 12 años. 
        Actualmente trabajo como freelance full-stack developer iOS y Android. 
        Además creo contenido formativo sobre programación y tecnología en redes. 
        Aquí podrás encontrar todos mis enlaces de interés. ¡Bienvenid@!""")
    )