def contar_letra_a(texto):
    #transforma a String em minúscula
    texto_minusculo = texto.lower()
    contador = 0

    # Percorre toda a String
    for caractere in texto_minusculo:
        if caractere == 'a':
            contador += 1

    # Verifica se a letra 'a' foi encontrada
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vezes.")
    else:
        print("A letra 'a' não foi encontrada.")

string_entrada = str(input("Digite uma palavra ou frase: "))
contar_letra_a(string_entrada)