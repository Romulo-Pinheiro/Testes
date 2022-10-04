try:
    x = int(input("Digite um valor para a coordenada X: "))
    y = int(input("Digite um valor para a coordenada Y: "))
    while x != 0 and y != 0:
        if x > 0:
            if y > 0:
                print("Primeiro Quadrante")
            else:
                print("Quarto Quadrante")
        else:
            if y > 0:
                print("Segundo Quadrante")    
            else:
                print("Terceiro Quadrante")
        x = int(input("Digite um valor para a coordenada X: "))
        y = int(input("Digite um valor para a coordenada Y: "))
except ValueError:
    print('Você deve informar um valor numérico')
except KeyboardInterrupt:
    print('\nPrograma Encerrado')