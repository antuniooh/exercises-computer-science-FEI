def validateString(string):
    estado = 0

    for char in string:
        if estado == 0:
            if char == 'i':
                estado = 1
            elif char == 'e':
                estado = 3
            elif char == 'f':
                estado = 7
            elif char == 't':
                estado = 9
            else:
                raise RuntimeError('Invalid char -> ' + char)
        elif estado == 1:
            if char == 'f':
                print('(if, PalavraReservada)')
            else:
                raise RuntimeError("Invalid char -> " + char)
        elif estado == 3:
            if char == 'l':
                estado = 4
            else:
                raise RuntimeError("Invalid char -> " + char)
        elif estado == 4:
            if char == 's':
                estado = 5
            else:
                raise RuntimeError("Invalid char -> " + char)
        elif estado == 5:
            if char == 'e':
                print('(Else, PalavraReservada)')
            else:
                raise RuntimeError("Invalid char -> " + char)
        elif estado == 7:
            if char == 'o':
                estado = 8
            else:
                raise RuntimeError("Invalid char -> " + char)
        elif estado == 8:
            if char == 'r':
                print('(For, PalavraReservada)')
            else:
                raise RuntimeError("Invalid char -> " + char)
        elif estado == 9:
            if char == 'h':
                estado = 10
            else:
                raise RuntimeError("Invalid char -> " + char)
        elif estado == 10:
            if char == 'e':
                estado = 11
            else:
                raise RuntimeError("Invalid char -> " + char)
        elif estado == 11:
            if char == 'n':
                print('(then, PalavraReservada)')
            else:
                raise RuntimeError("Invalid char -> " + char)
        else:
            raise RuntimeError("Invalid char -> " + char)


def main():
    with open("file.txt", "r") as file:
        for words in file.readlines():
            for word in words.split():
                try:
                    validateString(word)
                except RuntimeError as ex:
                    print(ex)


if __name__ == '__main__':
    main()
