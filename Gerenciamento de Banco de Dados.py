import pymysql

#Estou utilizando a bibilioteca pymysql para gerenciar o banco de dados
#Vou compilar o arquivo com a biblioteca pyinstaller 
com o script Python pronto va no terminal abra a pasta onde esta o script python
#Digite os comandos pip install pyinstaller
#Ao instalar digite pyinstaller -f `Nome do arquivo`
#o arquivo compilado para .exe esta na pasta dist



com_sql1 = ''
com_sql2 = 0
nome_table = ''
print("""
_______________________
| [1]Criar Tabela     |
| [2]Adicionar usuario|
| [3]Adicionar colunas|
| [4]Mostrar Tabelas  |
|_____________________|
        """)

def create_table():
    com_sql1 = f'CREATE TABLE {nome_table}(nome VARCHAR(255))'
    conexao = pymysql.connect(host='127.0.0.1', user='root', passwd='', database='recode')
    cursor = conexao.cursor()
    cursor.execute(com_sql1)

while True:
    try:
        menu = int(input('Digite a opção: '))
        break
    except:
        print('Digite apenas numeros')

if menu == 1:
    while True:
        try:
            nome_tabela = str(input('Qual o nome da tabela?')).lower()
            if nome_table.isnumeric():
                print('Não pode conter números!')
            else:
                nome_table = nome_tabela
                create_table()
                break
        except:
            print('Erro')

def ad_users():
    conexao = pymysql.connect(host='127.0.0.1', user='root', passwd='', database='recode')
    cursor = conexao.cursor()
    com_sql1 = f'ALTER TABLE usuários ADD COLUMN ({usuario} VARCHAR(255))'
    cursor.execute(com_sql1)

user = ''
if menu == 2:
    while True:
            usuario = str(input('Digite o nome de usuário: '))
            try:
                if usuario.strip() == '':
                    print('Erro')
                elif usuario.isnumeric():
                    print('Não pode conter números')
                else:
                    user = usuario
                    ad_users()
                    break
            except Exception as erro:
                print(erro)


def ad_column_idade():
    conexao = pymysql.connect(host='127.0.0.1', user='root', passwd='', database='recode')
    cursor = conexao.cursor()
    com_sql1 = f'ALTER TABLE idade ADD COLUMN ({nome_coluna} VARCHAR(255))'
    cursor.execute(com_sql1)


def ad_column_nome():
    conexao = pymysql.connect(host='127.0.0.1', user='root', passwd='', database='recode')
    cursor = conexao.cursor()
    com_sql1 = f'ALTER TABLE nome ADD COLUMN ({nome_coluna} VARCHAR(255))'
    cursor.execute(com_sql1)


def ad_column_sexo():
    conexao = pymysql.connect(host='127.0.0.1', user='root', passwd='', database='recode')
    cursor = conexao.cursor()
    com_sql1 = f'ALTER TABLE sexo ADD COLUMN ({nome_coluna} VARCHAR(255))'
    cursor.execute(com_sql1)



def show_tables():
    conexao = pymysql.connect(host='127.0.0.1', user='root', passwd='', database='recode')
    cursor = conexao.cursor()
    cursor.execute('SHOW TABLES')
    for x in cursor:
        print(x)



numero_coluna = 0
nome_coluna = ''
if menu == 3:
    while True:
            print("""
                    [1]Idade
                    [2]Nome
                    [3]Sexo
                    """)
            add_table = int(input('Em qual tabela você quer adicionar? '))
            if add_table == 1:
                try:
                    coluna = str(input('Digite o nome da coluna: ')).lower()
                    if coluna.isnumeric():
                        print('Não pode conter números!')
                    else:
                        nome_coluna = coluna
                        ad_column_idade()
                        break

                except:
                    print('Erro')
            elif add_table == 2:
                try:
                    coluna = str(input('Digite o nome da coluna: ')).lower()
                    if coluna.isnumeric():
                        print('Não pode conter números!')
                    else:
                        nome_coluna = coluna
                        ad_column_nome()
                        break
                except:
                    print('Erro')

            elif add_table == 3:
                try:
                    coluna = str(input('Digite o nome da coluna: ')).lower()
                    if coluna.isnumeric():
                        print('Não pode conter números!')
                    else:
                        nome_coluna = coluna
                        ad_column_sexo()
                        break
                except:
                    print('Erro')

if menu == 4:
    show_tables()

