from gtts import gTTS

texto = 'Olá somos os alunos do IFSP e adoramos a aula do professor Rafael Wendel'

obj = gTTS(text=texto, lang='pt', slow=False)

obj.save('welcome.mp3')
