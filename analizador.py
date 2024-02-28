from lark import Lark, Transformer
import os

# Obtén la ruta completa al archivo 'gramatica.lark'
current_dir = os.path.dirname(os.path.abspath(__file__))
gramatica_path = 'grammar.lark'

class AnalizadorSintactico(Transformer):
    def declaration(self, items):
        return "Declaración de variable analizada"

    def function(self, items):
        return "Función analizada"

    def loop(self, items):
        return "Bucle repeat analizado"

    def conditional(self, items):
        return "Condicional if-else analizado"

    def main(self, items):
        return "Función main analizada"

def analizar_entrada(entrada):
    # Usa la ruta completa al archivo 'gramatica.lark'
    grammar = open('grammar.lark').read()
    parser = Lark(grammar, start='start', parser='lalr', transformer=AnalizadorSintactico())

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

