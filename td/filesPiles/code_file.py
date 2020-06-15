def file_vide():
    return []

def file(valeur, file):
    return [valeur, file]

def push(valeur, file):
    if est_vide(file):
        return [valeur, file_vide()]
    return [file[0], push(valeur, file[1])]

def pop(file):
    return (file[0], file[1])

def est_vide(file):
    return file == file_vide()