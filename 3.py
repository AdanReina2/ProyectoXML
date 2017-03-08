#-*- coding:utf-8 -*-

# 3) Introducir una categoria por teclado y busca en el fichero cuantos monumentos tienen esa categoria.

from lxml import etree

cate = raw_input("Introducir una categoria: ")

doc = etree.parse("monumentos.xml")
raiz = doc.getroot()

for c in raiz.xpath("//categoria"):
	if cate == c.text:
		print (c.getparent().getparent()).find("nombre").text