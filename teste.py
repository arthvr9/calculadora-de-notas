import PySimpleGUI as sg

# Layout
sg.theme('Tan')
layout = [
    [sg.Text('Notas Primeiro Trimestre')],
    [sg.Text('Matemática'), sg.Input(key='matematica', text_color= 'purple')],
    [sg.Text('Química'), sg.Input(key='quimica')],
    [sg.Text('Inglês'), sg.Input(key='ingles')],
    [sg.Text('Português'), sg.Input(key='portugues')],
    [sg.Text('Geografia'), sg.Input(key='geografia')],
    [sg.Text('História'), sg.Input(key='historia')],
    [sg.Text('Geometria'), sg.Input(key='geometria')],
    [sg.Text('Linguagem'), sg.Input(key='linguagem')],
    [sg.Text('Inovação'), sg.Input(key='inovacao')],
    [sg.Text('Modelagem'), sg.Input(key='modelagem')],
    [sg.Text('Monitoramento'), sg.Input(key='monitoramento')],
    [sg.Text('Impactos'), sg.Input(key='impactos')],
    [sg.Text('Notas Segundo Trimestre')],
    [sg.Text('Matemática'), sg.Input(key='matematica2')],
    [sg.Text('Química'), sg.Input(key='quimica2')],
    [sg.Text('Inglês'), sg.Input(key='ingles2')],
    [sg.Text('Português'), sg.Input(key='portugues2')],
    [sg.Text('Geografia'), sg.Input(key='geografia2')],
    [sg.Text('História'), sg.Input(key='historia2')],
    [sg.Text('Geometria'), sg.Input(key='geometria2')],
    [sg.Text('Linguagem'), sg.Input(key='linguagem2')],
    [sg.Text('Inovação'), sg.Input(key='inovacao2')],
    [sg.Text('Modelagem'), sg.Input(key='modelagem2')],
    [sg.Text('Monitoramento'), sg.Input(key='monitoramento2')],
    [sg.Text('Impactos'), sg.Input(key='impactos2')],
    [sg.Button('Calcular notas')]
]

# Janela
janela = sg.Window('Calculadora de Notas', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Calcular notas':
        # Realizar o cálculo das notas e exibir os resultados aqui
        nota_matematica = float(valores['matematica']) + float(valores['matematica2'])
        nota_quimica = float(valores['quimica']) + float(valores['quimica2'])
        nota_ingles = float(valores['ingles']) + float(valores['ingles2'])
        nota_portugues = float(valores['portugues']) + float(valores['portugues2'])
        nota_geografia = float(valores['geografia']) + float(valores['geografia2'])
        nota_historia = float(valores['historia']) + float(valores['historia2'])
        nota_geometria = float(valores['geometria']) + float(valores['geometria2'])
        nota_linguagem = float(valores['linguagem']) + float(valores['linguagem2'])
        nota_inovacao = float(valores['inovacao']) + float(valores['inovacao2'])
        nota_modelagem = float(valores['modelagem']) + float(valores['modelagem2'])
        nota_monitoramento = float(valores['monitoramento']) + float(valores['monitoramento2'])
        nota_impactos = float(valores['impactos']) + float(valores['impactos2'])

        # Exibir os resultados em um pop-up
        resultado_texto = f"""Resultados:
        Matemática: {nota_matematica}
        Química: {nota_quimica}
        Inglês: {nota_ingles}
        Português: {nota_portugues}
        Geografia: {nota_geografia}
        História: {nota_historia}
        Geometria: {nota_geometria}
        Linguagem: {nota_linguagem}
        Inovação: {nota_inovacao}
        Modelagem: {nota_modelagem}
        Monitoramento: {nota_monitoramento}
        Impactos: {nota_impactos}"""

        sg.popup(resultado_texto, title='Resultados')

        media1 = 18 - nota_matematica
        media2 = 18 - nota_quimica
        media3 = 18 - nota_ingles
        media4 = 18 - nota_portugues
        media5 = 18 - nota_geografia
        media6 = 18 - nota_historia
        media7 = 18 - nota_geometria
        media8 = 18 - nota_linguagem
        media9 = 18 - nota_inovacao
        media10 = 18 - nota_modelagem
        media11 = 18 - nota_monitoramento
        media12 = 18 - nota_impactos

        # Verificar a parabenização
        if media1<= 0:
            parabenizacao_texto1 = "Você passou em Matemática"
        else:
            parabenizacao_texto1 = "Ainda faltam", media1, "pontos para passar de ano"
        if media2<= 0:
            parabenizacao_texto2 = "Você passou em Química"
        else:
            parabenizacao_texto2 = "Ainda faltam", media2, "pontos para passar de ano"
        if media3<= 0:
            parabenizacao_texto3 = "Você passou em Inglês"
        else:
            parabenizacao_texto3 = "Ainda faltam", media3, "pontos para passar de ano"
        if media4<= 0:
            parabenizacao_texto4 = "Você passou em Português"
        else:
            parabenizacao_texto4 = "Ainda faltam", media4, "pontos para passar de ano"
        if media5<= 0:
            parabenizacao_texto5 = "Você passou em Geografia"
        else:
            parabenizacao_texto5 = "Ainda faltam", media5, "pontos para passar de ano"
        if media6<= 0:
            parabenizacao_texto6 = "Você passou em História"
        else:
            parabenizacao_texto6 = "Ainda faltam", media6, "pontos para passar de ano"
        if media7<= 0:
            parabenizacao_texto7 = "Você passou em Geometria"
        else:
            parabenizacao_texto7 = "Ainda faltam", media7, "pontos para passar de ano"
        if media8<= 0:
            parabenizacao_texto8 = "Você passou em Linguagem"
        else:
            parabenizacao_texto8 = "Ainda faltam", media8, "pontos para passar de ano"
        if media9<= 0:
            parabenizacao_texto9 = "Você passou em Inovação"
        else:
            parabenizacao_texto9 = "Ainda faltam", media9, "pontos para passar de ano"
        if media10<= 0:
            parabenizacao_texto10 = "Você passou em Modelagem"
        else:
            parabenizacao_texto10 = "Ainda faltam", media10, "pontos para passar de ano"
        if media11<= 0:
            parabenizacao_texto11 = "Você passou em Monitoramento"
        else:
            parabenizacao_texto11 = "Ainda faltam", media11, "pontos para passar de ano"
        if media12<= 0:
            parabenizacao_texto12 = "Você passou em Impactos"
        else:
            parabenizacao_texto12 = "Ainda faltam", media12, "pontos para passar de ano"
        sg.popup(parabenizacao_texto1, title="Matemática")
        sg.popup(parabenizacao_texto2, title="Química")
        sg.popup(parabenizacao_texto3, title="Inglês")
        sg.popup(parabenizacao_texto4, title="Português")
        sg.popup(parabenizacao_texto5, title="Geografia")
        sg.popup(parabenizacao_texto6, title="História")
        sg.popup(parabenizacao_texto7, title="Geometria")
        sg.popup(parabenizacao_texto8, title="Linguagem")
        sg.popup(parabenizacao_texto9, title="Inovação")
        sg.popup(parabenizacao_texto10, title="Modelagem")
        sg.popup(parabenizacao_texto11, title="Monitoramento")
        sg.popup(parabenizacao_texto12, title="Impactos")


# Fechar a janela ao sair do loop
janela.close()
