import google.generativeai as genai

genai.configure(api_key="AIzaSyBKhyp0ErRyAkyydy8_3UFeI14UuFuReF4")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])

bem_vindo = "# Bem Vindo ao ODS 2030 Grau com Gemini AI #"
print(len(bem_vindo) * "#")
print(bem_vindo)
print(len(bem_vindo) * "#")
print("###   Digite 'sair' para encerrar    ###")
print("")

while True:
    texto = input("Escreva sua mensagem: ")

    if texto == "sair":
        break

    response = chat.send_message(texto)
    print("Gemini:", response.text, "\n")

print("Encerrando Chat")
