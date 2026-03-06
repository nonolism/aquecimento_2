import re


def atividade_1():

    RESERVADAS = {
                    "if", "else", "while", "for", "return", 
                    "int", "System", "out", "print", "public", "class"
                }

    codigo = """
    public class StarRectangle {
    public void printRectangle(int n) {
    for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
    System.out.print(" * ");
    }
    System.out.println();
    }
    }
    }
    """
    palavras = re.findall(r"[A-Za-z_]+", codigo)

    palavras_set = set(palavras)

    reservadas_encontradas = palavras_set & RESERVADAS
    identificadores = palavras_set - RESERVADAS

    print("Palavras reservadas encontradas:")
    print(reservadas_encontradas)

    print("\nPossíveis identificadores:")
    print(identificadores)

def atividade_2():
    usuario_A = {"Python", "Jogos", "Música", "IA"}
    usuario_B = {"Java", "IA", "Música", "Caminhada"}
    interesses_comum = usuario_A & usuario_B
    recomendacoes = usuario_B - usuario_A

    print("Interesses em comum:", interesses_comum)
    print("Recomendar para A:", recomendacoes)
    
def atividade_3():
    RH = {"ver_salario", "editar_perfil"}
    TI = {"acesso_servidor", "editar_perfil"}
    permissoes_totais = RH | TI
    print("Permissões totais:", permissoes_totais)
    permissoes_arquivo = {"ver_salario", "editar_perfil"}
    usuario = {"ver_salario", "editar_perfil"}
    if permissoes_arquivo.issubset(usuario):
        print("Usuário pode acessar o arquivo")
    else:
        print("Usuário NÃO pode acessar")
    
def atividade_4():
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    frase = "teste de frase"
    caracteres_frase = set(frase)
    caracteres_frase.discard(" ")

    if caracteres_frase <= alfabeto:
        print("Frase válida")
    else:
        print("Frase inválida")
        
atividade_1()
atividade_2()
atividade_3()
atividade_4()