import flet as ft
from flet import colors
from decimal import Decimal

botoes = [          # criando os botoes dentro de um dicionario para iterar depois um de cada vez
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
]

def main(page: ft.Page): # criando a função e o objeto da interface como parametro
    page.bgcolor = "#000"
    page.window_resizable = False
    page.window_width = 250
    page.window_height = 380
    page.title = 'Calculadora'
    page.window_always_on_top = True

    result = ft.Text(value = '0', color = colors.WHITE, size = 20) # para criar a variavel que exibe o resultado

    def calculate(operador, value_at):
        try:
            value = eval(value_at) # essa função recebe uma string como parametro e realiza a conta ex "2+2" 

            if operador == '%':
                value /= 100
            elif operador == '±':
                value = -value
        except:
            return 'Error'    # retornar erro caso ocorra uma conta invalida
        
        digits = min(abs(Decimal(value).as_tuple().exponent),5)
        return format(value, f'.{digits}f')

    def select(e): # função que é disparada quando ocorre um clique do mouse recebendo como parametro um evento
        value_at = result.value if result.value not in ('0', 'Error') else '' # vai pegar o valor que já esta no display
        value = e.control.content.value  # vai pegar o valor clicado no botao

        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/', '*', '-', '+', '.'):
                value_at = value_at[:-1]
            
            value = value_at + value

            if value[-1] in ('=', '%', '±'):
                value = calculate(operador=value[-1], value_at=value_at)

        result.value = value
        result.update()



    display = ft.Row(               # cria uma linha dentro da aplicação para alinhar o valor a esquerda
        width = 250,
        controls = [result],
        alignment = 'end'
    )

    btn = [ft.Container(              # cria um container em formato de lista para ser usado como botao
        content = ft.Text(value=btn['operador'], color=btn['fonte']),
        width = 45,
        height = 45,
        bgcolor = btn['fundo'],
        border_radius = 100,
        alignment = ft.alignment.center,
        on_click = select 
    )for btn in botoes] # nessa linha onde ocorre a iteração do dicionario acima com valor dos botoes, fundo e fonte

    keyboard = ft.Row(
        width = 250,
        wrap = True,            # caso estourar o limite de pixels e 'empurra' pra baixo
        controls = btn,         # recebe como lista todos os botoes
        alignment = 'end'
    )

    page.add(display, keyboard) # para adicionar a variavel display e keyboard na aplicação


ft.app(target = main) # para abrir a interface passando a função como argumento