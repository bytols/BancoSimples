import uuid
from datetime import datetime
import sqlite3

class Cliente:

    def __init__(self, nome):
        self.identificador = str(uuid.uuid4())
        self.nome = nome
        self.saldo = 0
        self.historico = []

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        self.historico.append(f"deposito de {valor} as {datetime.now()} na conta {self.identificador}")

    def sacar(self,valor):
        self.saldo = self.saldo - valor
        self.historico.append(f"saque de {valor} as {datetime.now()} na conta {self.identificador}")
    
    def saldo(self):
        print(f"seu saldo atual é de: {self.saldo}")


class Banco:

    def __init__(self) -> None:
        self.conexao = sqlite3.connect("banco.db")

    def criar_banco(self):
        with self.conexao:
            self.conexao.execute("""
            CREATE TABLE IF NOT EXISTS contas (
                id TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                saldo REAL NOT NULL
            );
            """)

    def inserir_conta(self, identificador, nome, saldo):
        with self.conexao:
            self.conexao.execute("INSERT INTO contas (id, nome, saldo) VALUES (?, ?, ?);", (identificador, nome, saldo))

    def listar_contas(self):
        with self.conexao:
            return self.conexao.execute("SELECT * FROM contas;").fetchall()

    def atualizar_saldo(self, conta_id, novo_saldo):
        with self.conexao:
            self.conexao.execute("UPDATE contas SET saldo = ? WHERE id = ?;", (novo_saldo, conta_id))

    def buscar_conta(self, conta_id):
        with self.conexao:
            return self.conexao.execute("SELECT * FROM contas WHERE id = ?;", (conta_id,)).fetchone()

    def fechar_banco(self):
        self.conexao.close()

