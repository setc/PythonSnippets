#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sebastián Torrente
#
# Created:     24/08/2012
# Copyright:   (c) Sebastián Torrente 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class PC(object):
    """Ficha del PNJ, contiene el nombre, los atributos y las habilidades"""

    def __init__(self, nombre, fue, agi, con, skills):
        self.nombre=nombre
        self.fue=fue
        self.agi=agi
        self.con=con
        self.skills=skills

    def __str__(self):
        return "Nombre: %s \n FUE: %s \n AGI: %s \n CON: %s \n Habilidades: %s" % (self.nombre,self.fue,self.agi,self.con,self.skills)

def main():
    Tian=Pj("Tian", 9, 11, 10, "Ataque: 125 \n Defensa: 125 \n Resistir Dolor: 100")
    print(Tian)

if __name__ == '__main__':
    main()
