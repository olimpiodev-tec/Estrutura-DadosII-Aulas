from gtts import gTTS

texto = 'Olá somos os alunos do IFSP'

obj = gTTS(text=texto, lang='pt', slow=False)

obj.save('welcome.mp3')
