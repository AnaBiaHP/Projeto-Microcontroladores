import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #renderiza a figura do matplotlib dentro de um widget tkinter
from serial import Serial

meu_serial=Serial("COM14", baudrate=9600, timeout=0.01)

eixoy = []
tempo=[]

lendo = False 
            
# Janela com tamanho inicial
janela = tk.Tk()
janela.title("Gráficos")
janela.geometry("800x400")

# Cria a figura do matplotlib
fig = Figure(figsize=(1, 2),dpi=100) #tamanho da figura para plotar o gráfico
ax = fig.add_subplot(1,1,1) #os 111 representam respectivamente linhas, colunas e posição inicial, área onde o gráfico está sendo desenhado

#Integra a figura no tkinter
canvas = FigureCanvasTkAgg(fig, master=janela) #FigureCanvasTkAgg renderiza a Figure do matplotlib usando o backend gráfico Agg e exibe o resultado dentro de um widget tkinter. O master=janela é o widget pai que o novo vai morar
canvas.draw() #converte todos os dados em uma figura
canvas.get_tk_widget().place(x=200, y=0, width=600, height=400) #pega a fig e move para o lugar que está marcando no place

# Campo Intervalo + label
etiqueta_intervalo = tk.Label(janela, text="Intervalo em Y:")
etiqueta_intervalo.place(x=20, y=10)

#início intervalo em y
etiqueta_intervalo = tk.Label(janela, text="Início:")
etiqueta_intervalo.place(x=20, y=25)

intervaloi = tk.IntVar()  # essa variável vai guardar o texto digitado pelo usuário
campo_intervalo = tk.Spinbox(janela, width=6, textvariable=intervaloi, from_=0, to=15)
campo_intervalo.place(x=22, y=45)

#fim intervalo em y
etiqueta_intervalo = tk.Label(janela, text="Fim:")
etiqueta_intervalo.place(x=20, y=70)

intervalof= tk.IntVar()  # essa variável vai guardar o texto digitado pelo usuário
campo_intervalo = tk.Spinbox(janela, width=6, textvariable=intervalof, from_=0, to=15)
campo_intervalo.place(x=22, y=90)

#captura os dados inseridos pelo usuário
def obter_dados():
  print("\n*** Dados do Usuário ***")
  print("Início Y:", intervaloi.get())
  print("Fim Y:", intervalof.get())
  
botao_dados = tk.Button(janela, text="Obter Dados", command=obter_dados)
botao_dados.place(x=22, y=160)

#(command é o jeito mais fácil de associar o clique a uma função)
def atualizar_grafico():
    iniy=intervaloi.get()
    fimy=intervalof.get()
    ax.clear() #necessário para o grafico atualizar e não desenhar uma curva em cima da outra
    if tipo_grafico == "I x t":
        ax.plot(tempo, eixoy, marker='o', color='steelblue')
        ax.set_title("Gráfico I x t")
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Corrente (mA)")
    elif tipo_grafico == "V x t":
        ax.plot(tempo, eixoy, marker='o', color='orange')
        ax.set_title("Gráfico V x t")
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Tensão (V)")
    elif tipo_grafico == "R x t":
        ax.plot(tempo, eixoy, marker='o', color='red')
        ax.set_title("Gráfico R x t")
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Resistência (Ohm)")
    elif tipo_grafico == "C x t":
        ax.plot(tempo, eixoy, marker='o', color='red')
        ax.set_title("Gráfico C x t")
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Capacitância (uF)")
    elif tipo_grafico == "D x t":
        ax.plot(tempo, eixoy, marker='o', color='blue')
        ax.set_title("Gráfico D x t")
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Diodo")
    ax.set_ylim(iniy, fimy)  # aplica o intervalo do eixo Y
    canvas.draw()
    
def ler_serial():
    global tipo_grafico
    if not lendo: #se for True o serial é lido, se for false, vai para o return e sai da função
        return
    retorno = meu_serial.readline() #retorna bytes
    if retorno != b"": #confirma que recebeu um byte
        texto_recebido=retorno.decode().strip() #equivalente a trim no arduino, usada para remover espaços em branco do início e do final do texto que são adicionados pelo b
        if texto_recebido.startswith("Comando"):
            tipo_grafico = texto_recebido[8: ]
        else:
            eixoy.append(float(texto_recebido))
            tempo.append(len(tempo)*1) #vai acrecentando os valores na lista
            atualizar_grafico() #a cada vez que um novo valor for lido ele é colocado no gráfico
    janela.after(10, ler_serial) #Daqui a 10 ms, execute ler_serial() novamente e enquanto isso a janela continua respondendo normalmente aos cliques, redimensionamentos e atualizações do gráfico.

def iniciar_leitura():
    global lendo
    lendo=True
    ler_serial()
    print("Começo da leitura")

botao1 = tk.Button(janela, text="Iniciar leitura", command=iniciar_leitura)
botao1.place(x=20, y=220)

def finalizar_leitura():
    global lendo
    lendo=False
    eixoy.clear() #Apaga os dados armazenados na lista tensoes
    tempo.clear() 
    ax.clear() #Apaga tudo o que foi desenhado no objeto Axes (linhas, título, legendas, eixos ...) -matplotlib
    canvas.draw() #Redesenha a figura na janela do Tkinter para mostrar as alterações feitas em ax.
    print("Fim da leitura")
    
botao1 = tk.Button(janela, text="Finalizar leitura", command=finalizar_leitura)
botao1.place(x=20, y=250)

janela.mainloop() #o programa só para de rodar quando a janela for fechada

"""
# Menu de gráficos + label
etiqueta_grafico = tk.Label(janela, text="Gráfico:")
etiqueta_grafico.place(x=20, y=110)

grafico = tk.StringVar(value="(selecione)")  # essa variável vai guardar a opção escolhida pelo usuário
campo_grafico = tk.OptionMenu(janela, grafico, "(selecione)", "I x t", "V x t", "R x t", "C x t", "D x t")
campo_grafico.config(width=10) #define a largura da lista suspensa criada para selecionar uma resposta
campo_grafico.place(x=20, y=125)


# Botão 2 (uma alternativa é usar o bind, para ter mais opções apertar, soltar, etc)
def imprimir_mensagem2(botao):
  print("Apertei o botão 2!")
  
def imprimir_mensagem3(botao):
  print("Soltei no botão 2!")

botao2 = tk.Button(janela, text="Botão 2")
botao2.place(x=100, y=10)
botao2.bind("<ButtonPress>", imprimir_mensagem2)
botao2.bind("<ButtonRelease>", imprimir_mensagem3)

# Campo Nome + label
etiqueta_nome = tk.Label(janela, text="Nome")
etiqueta_nome.place(x=20, y=60)

nome = tk.StringVar() # essa variável vai guardar o texto digitado pelo usuário
campo_nome = tk.Entry(janela, width=13, textvariable=nome)
campo_nome.place(x=20, y=80)

# Múltipla escolha do tipo do curso + label
concordo = tk.BooleanVar()
checkbox = tk.Checkbutton(janela, text='Concordo com os termos de uso', variable=concordo, onvalue=True, offvalue=False)
checkbox.place(x=400, y=80)
"""
