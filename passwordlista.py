#!-/usr/bin/python3

fich = open("/etc/passwd", "r");
lineas = fich.readlines();

for x in lineas:
	linea = x.split(':');
	print(linea[0]), ":" , linea[6];

fich.close();
