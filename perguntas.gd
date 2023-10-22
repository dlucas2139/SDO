extends Node2D

# Variável para armazenar a resposta correta
var resposta_correta = ""

# Estrutura de dados para armazenar perguntas, respostas e a resposta correta
var perguntas = [
	{
		"pergunta": "Qual é o nome do mascote icônico da Nintendo?",
		"respostas": ["A) Sonic", "B) Crash Bandicoot", "C) Link", "D) Mario"],
		"resposta_correta": "D) Mario",
		"resposta_errada": ["B) Crash Bandicoot","C) Link","D) Mario"]
		
		
		
	},

	
	{
		"pergunta": "Qual é o maior planeta do sistema solar?",
		"respostas": ["A) Terra", "B) Vênus", "C) Júpiter", "D) Marte"],
		"resposta_correta": "C) Júpiter"
	},
	{
		"pergunta": "Quem escreveu 'Romeu e Julieta'?",
		"respostas": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) F. Scott Fitzgerald"],
		"resposta_correta": "B) William Shakespeare"
	},
	{
		"pergunta": "Qual é o maior oceano do mundo?",
		"respostas": ["A) Oceano Atlântico", "B) Oceano Ártico", "C) Oceano Índico", "D) Oceano Pacífico"],
		"resposta_correta": "D) Oceano Pacífico"
	},
	{
		"pergunta": "Quantos continentes existem na Terra?",
		"respostas": ["A) 4", "B) 5", "C) 6", "D) 7"],
		"resposta_correta": "B) 5"
	},
	{
		"pergunta": "Qual é a capital do Brasil?",
		"respostas": ["A) São Paulo", "B) Rio de Janeiro", "C) Brasília", "D) Salvador"],
		"resposta_correta": "C) Brasília"
	},
	{
		"pergunta": "Quem pintou a 'Mona Lisa'?",
		"respostas": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
		"resposta_correta": "C) Leonardo da Vinci"
	},
	{
		"pergunta": "Qual é a maior cordilheira do mundo?",
		"respostas": ["A) Montanhas Rochosas", "B) Alpes", "C) Cordilheira dos Andes", "D) Montanhas Cárpatos"],
		"resposta_correta": "C) Cordilheira dos Andes"
	},
	{
		"pergunta": "Em que país a Torre Eiffel está localizada?",
		"respostas": ["A) Itália", "B) Espanha", "C) França", "D) Reino Unido"],
		"resposta_correta": "C) França"
	},
	{
		"pergunta": "Qual é o maior deserto do mundo?",
		"respostas": ["A) Deserto de Gobi", "B) Deserto do Saara", "C) Deserto de Kalahari", "D) Deserto de Atacama"],
		"resposta_correta": "B) Deserto do Saara"
	},
	{
		"pergunta": "Qual é a capital do Japão?",
		"respostas": ["A) Xangai", "B) Hong Kong", "C) Pequim", "D) Tóquio"],
		"resposta_correta": "D) Tóquio"
	}

	# Adicione mais perguntas aqui...
]

# Índice da pergunta atual
var pergunta_atual = -1

# Chamado quando o nó entra na árvore da cena pela primeira vez.
func _ready():
	mostrarProximaPergunta()

func mostrarProximaPergunta():
	# Avança para a próxima pergunta
	pergunta_atual += 1

	if pergunta_atual < perguntas.size():
		var pergunta = perguntas[pergunta_atual]
		resposta_correta = pergunta["resposta_correta"]

		$RichTextLabel.bbcode_text = pergunta["pergunta"]
		$RES_1.text = pergunta["respostas"][0]
		$RES_2.text = pergunta["respostas"][1]
		$RES_3.text = pergunta["respostas"][2]
		$RES_4.text = pergunta["respostas"][3]
		$acertou_errou.text = ""

		# Conecte o evento "pressed" de cada botão ao método "_on_Button_pressed"
		$RES_1.connect("pressed", self, "_on_Button_pressed", [$RES_1.text])
		$RES_2.connect("pressed", self, "_on_Button_pressed", [$RES_2.text])
		$RES_3.connect("pressed", self, "_on_Button_pressed", [$RES_3.text])
		$RES_4.connect("pressed", self, "_on_Button_pressed", [$RES_4.text])
	else:
		# Todas as perguntas foram respondidas
		$RichTextLabel.bbcode_text = "Todas as perguntas foram respondidas."
		$RES_1.text = ""
		$RES_2.text = ""
		$RES_3.text = ""
		$RES_4.text = ""
		

func _on_Button_pressed(answer):
	if answer == resposta_correta:
		
		
		$RES_1.disabled = true
		$RES_2.disabled = true
		$RES_3.disabled = true
		$RES_4.disabled = true
		
			
		# Resposta correta - Mostre a próxima pergunta
		$AudioStreamPlayer2D/certaresposta.play()
		
		yield(get_tree().create_timer(9.0), "timeout")
		$AudioStreamPlayer2D/certaresposta.stop()
		$RES_1.disabled = false
		$RES_2.disabled = false
		$RES_3.disabled = false
		$RES_4.disabled = false
		$RES_1.disconnect("pressed", self, "_on_Button_pressed")
		$RES_2.disconnect("pressed", self, "_on_Button_pressed")
		$RES_3.disconnect("pressed", self, "_on_Button_pressed")
		$RES_4.disconnect("pressed", self, "_on_Button_pressed")
		mostrarProximaPergunta()
		

##############

# Índice da pergunta atual
func _on_cartas_pressed():
	if pergunta_atual < perguntas.size():
		var pergunta = perguntas[pergunta_atual]
		var respostas_erradas = pergunta["resposta_errada"]
		
		# Embaralhe as respostas erradas
		#respostas_erradas.shuffle()
		
		# Número aleatório de respostas para bloquear
		var cartas_rand = randi() % 3 + 1
		
		# Bloqueie as respostas erradas com base no número aleatório
		for i in range(cartas_rand):
			if i < respostas_erradas.size():
				# Certifique-se de que a resposta não seja a correta
				if respostas_erradas[i] != pergunta["resposta_correta"]:
					bloquearRespostaErrada(respostas_erradas[i])
		

func bloquearRespostaErrada(resposta):
	if resposta == $RES_1.text:
		$RES_1.disabled = true
		$RES_1.disconnect("pressed", self, "_on_Button_pressed")
	elif resposta == $RES_2.text:
		$RES_2.disabled = true
		$RES_2.disconnect("pressed", self, "_on_Button_pressed")
	elif resposta == $RES_3.text:
		$RES_3.disabled = true
		$RES_3.disconnect("pressed", self, "_on_Button_pressed")
	elif resposta == $RES_4.text:
		$RES_4.disabled = true
		$RES_4.disconnect("pressed", self, "_on_Button_pressed")

	
	
	




