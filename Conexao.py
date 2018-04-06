class Conexao():

    #criar um arquivo vazio
    def criarArquivo():
        arquivo = open('dados_despesas.txt', 'w')
        arquivo.close()

    
    def retornarValores():
        base = 'dados_despesas.txt'
        try:
            #tenta abrir o arquivo de texto
            with open(base, 'r') as arquivo:
                #ler todas as linhas para uma lista
                valores = arquivo.readlines()
                arquivo.close()
        except IOError:
            print('Erro ao abrir o arqivo %s', base)
                

            

    def adicionarValor(valor):
        pass
