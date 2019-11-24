valor_plano_saude = 347.00
salario = float(input("Entre com o salário do colaorador: "))

total_descontado = 0

desconto_INSS = salario * 0.09
total_descontado += desconto_INSS

desconto_vale_transporte = salario * 0.03
total_descontado += desconto_vale_transporte

desconto_plano_saude = valor_plano_saude * 0.15
total_descontado += desconto_plano_saude

salario_liquido = salario - total_descontado

print("##################### HOLERITE #####################")
print("")
print("#### SALARIO INTEGRAL: ", salario)
print("----------------------------------------------------")
print("#### DESCONTOS")
print("#### INSS:               ", desconto_INSS)
print("#### PLANO DE SAÚDE:     ", desconto_plano_saude)
print("#### VALE TRANSPORTE:    ", desconto_vale_transporte)
print("#### TOTAL DESCONTADO:   ", total_descontado)
print("----------------------------------------------------")
print("")
print("#### SALARIO LIQUIDO: ", salario_liquido)
print("####################################################")
