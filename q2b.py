def main():
	a = int(input("selecione a conversão desejada: (1)libras para grama; (2) onça para grama: "))
	if a == 1:
		libras = float(input("Digite o valor em libras: "))
		grama = libras*453.592

		print("%.3f libras equivale a %.3f gramas"%(libras, grama))
	elif a == 2:
		onca = float(input("Digite o valor em onças: "))
		grama = onca*28.3495

		print("%.4f onças equivale a %.4f gramas"%(onca, grama))
	elif a != 1 and a != 2:
		print("operação invalida!!!!")
main()