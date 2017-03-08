#-*- coding:utf-8 -*-

# 4) Introducir por teclado un nombre de monumentos y mostrar por pantalla la localización y el identificador de ese monumento.

from lxml import etree

monu = raw_input("Introducir un nombre de monumentos: ")

doc = etree.parse("monumentos.xml")
raiz = doc.getroot()
consu = raiz.xpath("//directorio")

for c in consu:
	if c.find("nombre").text == monu:
		print "Localización: " + str(c.find("localizacion").text)
		print "Identificador: " + str(c.find("identificador").text)