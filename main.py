import flet as ft

def main(page: ft.Page):
    page.title = "Pet Shop Confiável"
    
    # Definindo o tema com a paleta de cores personalizada
    page.theme = ft.Theme(
        color_scheme_seed="#87CEEB",  # Azul Claro (cor base do tema)
        primary="#87CEEB",            # Azul Claro
        secondary="#98FB98",          # Verde Menta
        background="#F5F5F5",         # Cinza Claro para o fundo principal
        surface="#FFDAB9",            # Laranja Pastel para áreas em destaque
        on_surface="#D2B48C",         # Marrom Claro para textos em áreas secundárias
    )

    # Exemplo de componentes usando o tema personalizado
    page.add(
        ft.Text("Bem-vindo ao Pet Shop Confiável!", size=30, color=page.theme.primary),
        ft.ElevatedButton("Agendar Consulta", bgcolor=page.theme.secondary, color="white"),
        ft.Container(
            content=ft.Text("Destaque importante", color="white"),
            bgcolor=page.theme.surface,
            padding=10,
            border_radius=5,
        )
    )

ft.app(target=main)
