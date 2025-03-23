# importando a biblioteca atribuindo um apelido com o 'as'
import speedtest as st

test = st.Speedtest()


def logo_menu():
	print('\n\t\t+--------------+')
	print('\t\t|NET-SPEED v1.0|')
	print('\t\t+--------------+')

def help():
	print('\nComandos:')
	print('\t--net-speed ou -ns     '
	'Exibe velocidade de DOWNLOAD, UPLOAD e PING.\n\t--help ou -h     '
	'Exibe ajuda sobre a aplicação.\n\t--exit ou -e     Finaliza a instância atual da aplicação.')

def download():
	# Obtendo a velocidade de download e convertendo para MB/s
	print('\nAguarde...\n')
	print(f'Velocidade de Download: {(test.download() / 8**6):.2f} MB')

def upload():
	# Obtendo a velocidade de upload e convertendo para MB/s
	print(f'Velocidade de Upload: {(test.upload() / 8**6):.2f} MB')

def ping():
	# Obtendo o ping da conexão, em mili-segundos
	ping = test.results.ping
	print(f'Ping: {ping:.2f} ms')

def options():

	while(True):
		print('\n')
		op_user = input('>>')

		# Abre opcao ajuda
		if op_user == '--help' or op_user == '-h':
			help()
	
		elif op_user == '--net-speed' or op_user == '-ns':
			download()
			upload()
			ping()
	
		elif op_user == '--exit'or op_user == '-e':
			print('\nClose aplication.')
			break
		else:
			help()

def main():
	logo_menu()
	options()
	
	

if __name__=="__main__":
		main()
