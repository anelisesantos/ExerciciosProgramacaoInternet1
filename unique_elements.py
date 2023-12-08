# Inicializa a lista original e a nova lista
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

# Percorre cada elemento na lista original
for i in my_list:
    # Verifica se o elemento não está na nova lista
    if i not in new_list:
        # Adiciona o elemento à nova lista se ele for único
        new_list.append(i)

# Imprime a nova lista com elementos únicos
print("The list with unique elements only:")
print(new_list)
