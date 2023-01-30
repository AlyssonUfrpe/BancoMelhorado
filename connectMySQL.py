import mysql.connector as connect_db

class Connect:
    def __init__(self):
        self.db = connect_db.connect(
            host=' db4free.net',
            port=3306,
            user='alisson',
            passwd='alissonsilva',
            db='banco_contas'
        )
        self.cursor = self._db.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS CONTA(ID INT PRIMARY KEY NOT NULL, SALDO REAL NOT NULL, CONTA_POUPANCA INT NOT NULL, CONTA_BONIFICADA INT NOT NULL);''')
    
    def criaConta(self,id,is_poupanca,is_bonificada,saldo):
        self.cursor.execute('''INSERT INTO CONTA  (ID,SALDO,CONTA_POUPANCA,CONTA_BONIFICADA) VALUES ({},{},{},{});'''.format(str(id),str(saldo),str(is_poupanca),str(is_bonificada)))
        self.db.commit()
    
    def transferencia(self,saldo,id):
        try:
            self.cursor.execute('''UPDATE CONTA SET SALDO = {} WHERE ID = {};'''.format(str(saldo),str(id)))
            self.db.commit()
            print("movimentação concluida")
            return saldo
        except :
            return("Erro")
        

    def consultarSaldo(self,id):
        try:
            conta_bancaria= self.cursor.execute('''SELECT * FROM CONTA WHERE ID={}'''.format(str(id)))
            w = self.cursor.fetchall()[0]
            k = w[1]
            return k
        except:
            return("Essa conta não existe! ")

    def retornarContaP(self,id):
        conta_bancaria = self.cursor.execute('''SELECT * FROM CONTA WHERE ID={} AND CONTA_POUPANCA=1'''.format(str(id)))
        try:
            w =  self.cursor.fetchall()[0]
            return w
        except:
            return -1
    def retornarContaB(self,id):
        conta_bancaria = self.cursor.execute('''SELECT * FROM CONTA WHERE ID={} AND CONTA_BONIFICADA=1'''.format(str(id)))
        try:
            w =  self.cursor.fetchall()[0]
            return w
        except:
            return -1
    def rendimentoP(self,id,saldo):
        self.cursor.execute('''UPDATE CONTA SET SALDO = {} WHERE ID = {};'''.format(str(saldo),str(id)))
        self.db.commit()

    def rendimentoB(self,id,saldo):
        self.cursor.execute('''UPDATE CONTA SET SALDO = {} WHERE ID = {};'''.format(str(saldo),str(id)))
        self.db.commit()

    def verificaExistencia(self,id):
        conta_bancaria = self.cursor.execute('''SELECT * FROM CONTA WHERE ID={}'''.format(str(id)))
        try:
            y = self.cursor.fetchall()[0]
            return y
        except Exception as erro:
            print(erro)
            return -1
    
