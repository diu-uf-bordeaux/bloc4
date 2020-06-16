class File:
    file_vide = None

    def __init__(self, valeur, file):
        self._valeur = valeur
        self._suite = file

    def push(self, valeur):
        if File.est_vide(self._suite):
            self._suite = File(valeur, File.file_vide)
        else:
            self._suite.push(valeur)
        return self

    def pop(self):
        return (self._valeur, self._suite)

    def est_vide(file):
        return file is File.file_vide