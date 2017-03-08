#-*- coding:utf-8 -*-

# 2) Programa que cuenta todos los monumentos.

from lxml import etree

doc = etree.parse("monumentos.xml")
raiz = doc.getroot()

contador = 0

for c in raiz.xpath("//nombre"):
	contador = contador + 1

print "Hay un total de " + str(contador) + " monumentos."