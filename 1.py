#-*- coding:utf-8 -*-

# 1) Programa que lista todas los monumentos.

from lxml import etree

doc = etree.parse("monumentos.xml")
raiz = doc.getroot()

for c in raiz.xpath("//nombre"):
	print c.text