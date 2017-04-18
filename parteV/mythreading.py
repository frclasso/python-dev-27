#!/usr/bin/python

# -*- coding: utf-8 -*-

#exemplo de uso de threads
import os, time, threading

class Monitor(threading.Thread):
	#class de monitoramento usando Threads
	def __init__(self, ip):
		#construtor da trhead
		#atributos da thread
		self.ip = ip
		self.status = None
		#inicializador da classe thread
		threading.Thread.__init__(self)

	def run(self):
		#codigo sera executado pela thread
		#executa o ping
		ping = os.popen('ping -c1 %s' % self.ip).read()

		if 'Esgotado' in ping:
			self.status = False
		else:
			self.status = True


if __name__ == "__main__":

	#cria uma lista com um objeto thread para cada ip
	monitores = []
	for i in range(1,11):
		ip = '192.168.25.%d'%i
		monitores.append(Monitor(ip))

		#executa as threads
		for monitor in monitores:
			monitor.start()

		"""A thread principal continua enquanto as outras threads executam ping
		para os enderecos da lista"""

		#Verifique a cada segundo se as threds acabaram
		ping = True
		while ping:
			ping = False
			for monitor in monitores:
				if monitor.status == None:
				    ping =True
				    break
			time.sleep(1)
				    
        #imprime os resultados no final
        for monitor in monitores:
        	if monitor.status:
        		print'%s no ar'%monitor.ip
        	else:
        		print'%s fora do ar'%monitor.ip