# analizar_entrada.py
from lark import Lark
from analizador import AnalizadorSintactico

# Leer la gramática desde el archivo
with open('gramatica.lark', 'r') as grammar_file:
    GRAMMAR = grammar_file.read()

def analizar_entrada(entrada):
    parser = Lark(GRAMMAR, start='start', parser='lalr', transformer=AnalizadorSintactico())

    try:
        tree = parser.parse(entrada)
        return tree
    except Exception as e:
        return f"Error de sintaxis: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    entrada = """
    int $numero = 10;

    func suma(int $a, int $b){
        retornar $a + $b;
    }

    repeat (int $i = 0; $i < 10; $i++) {
        echo($i);
    }

    if ($numero > 5) {
        echo("El número es mayor a 5");
    } else {
        echo("El número es menor a 5");
    }

    func main() {
        echo("Inicio del programa");
    }
    """

    resultado = analizar_entrada(entrada)
    print(resultado)
