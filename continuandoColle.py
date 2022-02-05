usuarios_data_science = [15, 23 , 43, 56]
usuarios_machine_learrning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learrning)

for usuario in set(assistiram):
    print(usuario)

#set([1, 2, 3, 1]) - imprime {1, 2, 3}
