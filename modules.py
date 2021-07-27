import mysql.connector

class InserirDados: #Classe para conexão e insersão de registros no banco de dados
    
    def __init__(self): #Fará a conexão
        self.cnx = mysql.connector.connect(host = 'localhost', database = 'cadastro', user = 'seu_user', password = 'sua_senha')
        self.cursor = self.cnx.cursor()

    def insert_into(self, data_produto): #Fará a inserção dos registros 
        
        #Comando sql
        add_produto = "INSERT INTO produtos VALUES(DEFAULT, %(nome)s, %(descricao)s, %(categoria)s, %(preco)s);"

        #Dados


        #Execução
        self.cursor.execute(add_produto, data_produto)

        self.cnx.commit()

        self.cursor.close()
        self.cnx.close()

