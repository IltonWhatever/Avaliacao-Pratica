def searchfuncionario(id,lista_funcionario):
    id_funcionario = id
    id_funcionario = int(id_funcionario)
    funcionario = [item for item in lista_funcionario if item[0] == id_funcionario]
    return funcionario
