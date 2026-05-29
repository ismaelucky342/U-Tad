MAP(input_line):

    words = split(input_line)

    for each word in words:
        emit(word, 1)



SHUFFLE:

    agrupar todos los valores por clave (palabra)



REDUCE(key, values):

    sum = 0

    for each v in values:
        sum = sum + v

    emit(key, sum)