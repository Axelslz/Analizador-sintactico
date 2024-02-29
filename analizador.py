from lark import Transformer, Lark

def load_grammar():
    with open("grammar.lark", "r") as file:
        return file.read()


class MyTransformer(Transformer):
    def declaracion(self, items):
        # items contiene los tokens para INT, DOLLAR, LETRA, IGUAL, NUMERO, PUNTOYCOMA
        variable = items[1]  # Nombre de la variable
        valor = items[3]  # Valor asignado
        return f"Declaración de variable: {variable}, con valor: {valor}"

    def funcion(self, items):
        # items contiene los tokens y subárboles para FUNC, LETRA, parametros, retorno
        nombre_funcion = items[1]  # Nombre de la función
        parametros = items[2] if len(items) > 3 else []  # Lista de parámetros
        cuerpo = items[3] if len(items) > 3 else items[2]  # Cuerpo/retorno de la función
        return f"Función: {nombre_funcion}, Parámetros: {parametros}, Cuerpo: {cuerpo}"

    def bucle(self, items):
        # items contiene los tokens y subárboles para REPEAT, declaracion, condicion, incremento, echo_stmt
        declaracion = items[1]
        condicion = items[2]
        incremento = items[3]
        cuerpo = items[4:]  # Todos los echo_stmt dentro del bucle
        return f"Bucle con declaración: {declaracion}, condición: {condicion}, incremento: {incremento}, cuerpo: {cuerpo}"

    def condicional(self, items):
        # items contiene los tokens y subárboles para IF, condicion, echo_stmt, y opcionalmente ELSE
        condicion = items[1]
        verdadero = items[2]
        falso = items[3] if len(items) > 3 else None
        return f"Condicional: si {condicion}, entonces {verdadero}, sino {falso}"

    def funcion_main(self, items):
        # items contiene los tokens y subárboles para FUNC, MAIN, echo_stmt
        cuerpo = items[2:]  # Todos los echo_stmt dentro de main
        return f"Función main con cuerpo: {cuerpo}"

    def echo_stmt(self, items):
        # items contiene los tokens para ECHO, (LETRA | DOLLAR LETRA | CADENA)
        contenido = items[1]
        return f"Imprimir: {contenido}"

    def parametros(self, items):
        # Devuelve una lista de parámetros
        return ", ".join([f"{tipo} {nombre}" for tipo, nombre in items])

    def retorno(self, items):
        # items contiene los tokens para RETURN y expresion
        expresion = items[1]
        return f"Retornar: {expresion}"

    def condicion(self, items):
        # items contiene DOLLAR, LETRA, OPERADOR, NUMERO
        variable = items[1]
        operador = items[2]
        numero = items[3]
        return f"{variable} {operador} {numero}"

    def incremento(self, items):
        # items contiene DOLLAR, LETRA, MAS+
        variable = items[1]
        operacion = ''.join(items[2:])
        return f"Incremento de: {variable} con operación: {operacion}"
    
def analizar_entrada(entrada):
    try:
        grammar = load_grammar()
        # Asegúrate de que la regla de inicio es 'inicio'
        parser = Lark(grammar, parser='lalr', start='inicio', transformer=MyTransformer())
        tree = parser.parse(entrada)
        return "Correcto"
    except Exception as e:
        return str(e)