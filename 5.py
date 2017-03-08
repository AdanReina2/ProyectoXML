#-*- coding:utf-8 -*-

# 5) Mostrar en pantalla todos los monumentos con las categorias que tiene.

from lxml import etree

doc = etree.parse("monumentos.xml")
raiz = doc.getroot()
consu = raiz.xpath("//directorio")

for c in consu:
	print "Nombre: ", c.find("nombre").text
	print "Categorias: "
	for d in c.find("categorias"):
		print d.text
	print ""