letras="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
digitos="0123456789"
guion_bajo="_"
ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA" # La distinción entre estado trampa y no final es porque si bien en ambos casos la cadena 
                                   # actual no es aceptada, estando en un estado final ante el siguiente carácter de entrada el 
                                   # estado puede cambiar, mientras en el trampa no pues es un pozo
    
def AUTOMATA_SUMA(lexema):
    estado=0
    estados_finales = [1]
    for caracter in lexema:
        if estado==0 and caracter=="+":
            estado=1
        else:
            estado=-1
            break
    if estado==-1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
def AUTOMATA_RESTA(lexema):
    estado=0
    estados_finales=[1]
    for caracter in lexema:
        if estado==0 and caracter=="-":
            estado=1
        else:
            estado=-1
            break
    if estado==-1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
def AUTOMATA_MULTI(lexema):
    estado=0
    estados_finales=[1]
    for caracter in lexema:
        if estado==0 and caracter=="*":
            estado=1
        else:
            estado=-1
            break
    if estado==-1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
     
def AUTOMATA_NUM(lexema):
    estado = 0
    estados_finales = [1]
    
    for c in lexema:
        if estado == 0:
            if c == "0":
                estado = 1
            elif c == "1":
                estado = 1
            elif c == "2":
                estado = 1
            elif c == "3":
                estado = 1
            elif c == "4":
                estado = 1
            elif c == "5":
                estado = 1
            elif c == "6":
                estado = 1
            elif c == "7":
                estado = 1
            elif c == "8":
                estado = 1
            elif c == "9":
                estado = 1
            else:
                estado = -1
                break
        elif estado == 1:
            if c == "0":
                estado = 1
            elif c == "1":
                estado = 1
            elif c == "2":
                estado = 1
            elif c == "3":
                estado = 1
            elif c == "4":
                estado = 1
            elif c == "5":
                estado = 1
            elif c == "6":
                estado = 1
            elif c == "7":
                estado = 1
            elif c == "8":
                estado = 1
            elif c == "9":
                estado = 1
            else:
                estado = -1
                break

    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_PROGRAM(lexema):
    estados=0
    estados_finales=[7]
    for c in lexema:
        if estados==0 and c=="p":
            estados=1
        elif estados==1 and c=="r":
            estados=2
        elif estados==2 and c=="o":
            estados=3
        elif estados==3 and c=="g":
            estados=4
        elif estados==4 and c=="r":
            estados=5
        elif estados==5 and c=="a":
            estados=6
        elif estados==6 and c=="m":
            estados=7
        else:
            estados=-1
            break
    if estados==-1:
        return ESTADO_TRAMPA
    elif estados in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
def AUTOMATA_LEFTP(lexema):
    estado=0
    estados_finales=[1]
    for c in lexema:
        if estado == 0 and c=="(":
            estado=1
        else:
            estado=-1
            break
    if estado==-1:
        return ESTADO_TRAMPA
    else:
        if estado in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def AUTOMATA_RIGHTP(lexema):
    estado=0
    estados_finales=[1]
    for c in lexema:
        if estado == 0 and c==")":
            estado=1
        else:
            estado=-1
            break
    if estado==-1:
        return ESTADO_TRAMPA
    else:
        if estado in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def AUTOMATA_VAR(lexema):
    estado=0
    estados_finales=[3]
    for c in lexema:
        if estado==0 and c=="v":
            estado=1
        elif estado==1 and c=="a":
            estado=2
        elif estado==2 and c=="r":
            estado=3
        else:
            estado=-1
            break
    if estado==-1:
        return ESTADO_TRAMPA
    else:
        if estado in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL
        
def AUTOMATA_IF(lexema):
    estado=0
    estados_finales=[2]
    for c in lexema:
        if estado==0 and c=="i":
            estado=1
        elif estado==1 and c=="f":
            estado=2
        else:
            estado=-1
            break
    if estado==-1:
        return ESTADO_TRAMPA
    else:
        if estado in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def AUTOMATA_ELSE(lexema):
    estado=0
    estados_aceptados=[4]
    for c in lexema:
        if estado==0 and c=="e":
            estado=1
        elif estado==1 and c=="l":
            estado=2
        elif estado==2 and c=="s":
            estado=3
        elif estado==3 and c=="e":
            estado=4
        else:
            estado=-1
            break
    if estado==-1:
        return ESTADO_TRAMPA
    else:
        if estado in estados_aceptados:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL
        
def AUTOMATA_END(lexema):
    estado=0
    estados_aceptados=[3]
    for c in lexema:
        if estado==0 and c=="e":
            estado=1
        elif estado==1 and c=="n":
            estado=2
        elif estado==2 and c=="d":
            estado=3
        else:
            estado=-1
            break
    if estado==-1:
        return ESTADO_TRAMPA
    else:
        if estado in estados_aceptados:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL
        
def AUTOMATA_BEGIN(lexema):
    estado = 0
    estados_finales = [5]
    for c in lexema:
        if estado == 0 and c == 'b':
            estado = 1
        elif estado == 1 and c == 'e':
            estado = 2
        elif estado == 2 and c == 'g':
            estado = 3
        elif estado == 3 and c == 'i':
            estado = 4
        elif estado == 4 and c == 'n':
            estado = 5
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_TRUE(lexema):
    estado = 0
    estados_finales = [4]
    for c in lexema:
        if estado == 0 and c == 't':
            estado = 1
        elif estado == 1 and c == 'r':
            estado = 2
        elif estado == 2 and c == 'u':
            estado = 3
        elif estado == 3 and c == 'e':
            estado = 4
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_FALSE(lexema):
    estado = 0
    estados_finales = [5]
    for c in lexema:
        if estado == 0 and c == 'f':
            estado = 1
        elif estado == 1 and c == 'a':
            estado = 2
        elif estado == 2 and c == 'l':
            estado = 3
        elif estado == 3 and c == 's':
            estado = 4
        elif estado == 4 and c == 'e':
            estado = 5
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_AND(lexema):
    estado = 0
    estados_finales = [3]
    for c in lexema:
        if estado == 0 and c == 'a':
            estado = 1
        elif estado == 1 and c == 'n':
            estado = 2
        elif estado == 2 and c == 'd':
            estado = 3
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_NOT(lexema):
    estado = 0
    estados_finales = [3]
    for c in lexema:
        if estado == 0 and c == 'n':
            estado = 1
        elif estado == 1 and c == 'o':
            estado = 2
        elif estado == 2 and c == 't':
            estado = 3
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_OR(lexema):
    estado = 0
    estados_finales = [2]
    for c in lexema:
        if estado == 0 and c == 'o':
            estado = 1
        elif estado == 1 and c == 'r':
            estado = 2
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_MENOR(lexema):
    estado = 0
    estados_finales = [1]
    for c in lexema:
        if estado == 0 and c == "<":
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_MAYOR(lexema):
    estado = 0
    estados_finales = [1]
    for c in lexema:
        if estado == 0 and c == ">":
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_MENOR_IGUAL(lexema):
    estado = 0
    estados_finales = [2]
    for c in lexema:
        if estado == 0 and c == "<":
            estado = 1
        elif estado == 1 and c == "=":
            estado = 2
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_MAYOR_IGUAL(lexema):
    estado = 0
    estados_finales = [2]
    for c in lexema:
        if estado == 0 and c == ">":
            estado = 1
        elif estado == 1 and c == "=":
            estado = 2
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_IGUAL(lexema):
    estado = 0
    estados_finales = [2]
    for c in lexema:
        if estado == 0 and c == "=":
            estado = 1
        elif estado == 1 and c == "=":
            estado = 2
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_DISTINTO(lexema):
    estado = 0
    estados_finales = [2]
    for c in lexema:
        if estado == 0 and c == "<":
            estado = 1
        elif estado == 1 and c == ">":
            estado = 2
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_BOOL(lexema):
    estado = 0
    estados_finales = [4]
    for c in lexema:
        if estado == 0 and c == 'b':
            estado = 1
        elif estado == 1 and c == 'o':
            estado = 2
        elif estado == 2 and c == 'o':
            estado = 3
        elif estado == 3 and c == 'l':
            estado = 4
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
def AUTOMATA_ID(lexema):
    estado = 0
    estados_finales = [1]
    
    for c in lexema:
        if estado == 0:
            if c in letras or c == "_":
                estado = 1
            else:
                estado = -1
                break
        elif estado == 1:
            if c in letras or c in digitos or c == "_":
                estado = 1
            else:
                estado = -1
                break
    
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def AUTOMATA_INT(lexema):
    estado = 0
    estados_finales = [3]
    for c in lexema:
        if estado == 0 and c == 'i':
            estado = 1
        elif estado == 1 and c == 'n':
            estado = 2
        elif estado == 2 and c == 't':
            estado = 3
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_ASSIGN(lexema):
    estado = 0
    estados_finales = [1]
    for c in lexema:
        if estado == 0 and c == '=':
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_SEMIDOT(lexema):
    estado = 0
    estados_finales = [1]
    for c in lexema:
        if estado == 0 and c == ';':
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_RANGE(lexema):
    estado = 0
    estados_finales = [3]
    for c in lexema:
        if estado == 0 and c == '.':
            estado = 1
        elif estado == 1 and c == '.':
            estado = 2
        elif estado == 2 and c == '.':
            estado = 3
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_ESPACIO(lexema):
    estado = 0
    estados_finales = [1]
    for c in lexema:
        if estado == 0 and c == ' ':
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_TAB(lexema):
    estado = 0
    estados_finales = [1]
    for c in lexema:
        if estado == 0 and c == '\t':
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_RETORNO_DE_CARRO(lexema):
    estado = 0
    estados_finales = [1]
    for c in lexema:
        if estado == 0 and c == '\n':
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_GOTO(lexema):
    estado = 0
    estados_finales = [4]
    for c in lexema:
        if estado == 0 and c == 'g':
            estado = 1
        elif estado == 1 and c == 'o':
            estado = 2
        elif estado == 2 and c == 't':
            estado = 3
        elif estado == 3 and c == 'o':
            estado = 4
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_LET(lexema):
    estado = 0
    estados_finales = [3]
    for c in lexema:
        if estado == 0 and c == 'l':
            estado = 1
        elif estado == 1 and c == 'e':
            estado = 2
        elif estado == 2 and c == 't':
            estado = 3
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_DOSPUNTOS(lexema):
    estado = 0
    estados_finales = [1]
    for c in lexema:
        if estado == 0 and c == ':':
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_PUNTO(lexema):
    estado = 0
    estados_finales = [1]
    for c in lexema:
        if estado == 0 and c == '.':
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def AUTOMATA_ASSIGN_EXT(lexema):
    estado = 0
    estados_finales = [2]
    for c in lexema:
        if estado == 0 and c == ':':
            estado = 1
        elif estado == 1 and c == '=':
            estado = 2
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def obtener_token_mas_largo(codigo_fuente, inicio):
    mejor_token = None
    mejor_lexema = ""
    for j in range(inicio+1, len(codigo_fuente)+1):
        lexema = codigo_fuente[inicio:j]
        for (nombre_token, automata) in TOKENS_POSIBLES:
            if automata(lexema) == ESTADO_FINAL:
                if len(lexema) > len(mejor_lexema):
                    mejor_token = nombre_token
                    mejor_lexema = lexema
    return mejor_token, mejor_lexema

def lexer(codigo_fuente):
    tokens = []
    posicion_actual = 0
    while posicion_actual < len(codigo_fuente):
        mejor_token, mejor_lexema = obtener_token_mas_largo(codigo_fuente, posicion_actual)
        if mejor_token is None or mejor_lexema == "":
            raise Exception("ERROR:TOKEN DESCONOCIDO " + codigo_fuente[posicion_actual])
        if mejor_token not in ["SPACE_R", "SPACE_E", "SPACE_T"]:
            tokens.append((mejor_token, mejor_lexema))
        posicion_actual += len(mejor_lexema)
    tokens.append(('Eof','Eof'))
    return tokens

TOKENS_POSIBLES = [
    ("MATH_PLUS", AUTOMATA_SUMA),
    ("MATH_MINUS", AUTOMATA_RESTA),
    ("MATH_MULT", AUTOMATA_MULTI),
    ("NUM", AUTOMATA_NUM),
    ("PROGRAM", AUTOMATA_PROGRAM),
    ("LPAREN", AUTOMATA_LEFTP),
    ("RPAREN", AUTOMATA_RIGHTP),
    ("VAR", AUTOMATA_VAR),
    ("IF", AUTOMATA_IF),
    ("ELSE", AUTOMATA_ELSE),
    ("END", AUTOMATA_END),
    ("BEGIN", AUTOMATA_BEGIN),
    ("TRUE", AUTOMATA_TRUE),
    ("FALSE", AUTOMATA_FALSE),
    ("AND", AUTOMATA_AND),
    ("NOT", AUTOMATA_NOT),
    ("OR", AUTOMATA_OR),
    ("REL_MEN", AUTOMATA_MENOR),
    ("REL_MAY", AUTOMATA_MAYOR),
    ("REL_MENIG", AUTOMATA_MENOR_IGUAL),
    ("REL_MAYIG", AUTOMATA_MAYOR_IGUAL),
    ("REL_IG", AUTOMATA_IGUAL),
    ("REL_DIS", AUTOMATA_DISTINTO),
    ("BOOL", AUTOMATA_BOOL),
    ("INT", AUTOMATA_INT),
    ("ASSIGN", AUTOMATA_ASSIGN),
    ("SEMIDOT", AUTOMATA_SEMIDOT),
    ("RANGE", AUTOMATA_RANGE),
    ("SPACE_R", AUTOMATA_RETORNO_DE_CARRO),
    ("SPACE_E", AUTOMATA_ESPACIO),
    ("SPACE_T", AUTOMATA_TAB),
    ("GOTO", AUTOMATA_GOTO),
    ("LET", AUTOMATA_LET),
    ("COLON", AUTOMATA_DOSPUNTOS),
    ("DOT", AUTOMATA_PUNTO),
    ("ASSIGN_EXT", AUTOMATA_ASSIGN_EXT),
    ("ID", AUTOMATA_ID),
]

print(lexer("cadena de prueba"))

#PRUEBAS DEL LEXER

def mostrar_prueba(nombre, codigo):
    print(f"\n--- {nombre} ---")
    print("Entrada:")
    print(codigo)
    try:
        resultado = lexer(codigo)
        print("Salida:")
        for token in resultado:
            print(token)
    except Exception as e:
        print("Error:", e)

# Prueba 1: Programa mínimo
codigo1 = "program ejemplo.\nbegin\nend"
mostrar_prueba("Prueba 1: Programa mínimo", codigo1)

# Prueba 2: Declaración de variable int
codigo2 = "var x : int(1...10) = 5;"
mostrar_prueba("Prueba 2: Declaración de variable int", codigo2)

# Prueba 3: Declaración de variable bool
codigo3 = "var b : bool = true;"
mostrar_prueba("Prueba 3: Declaración de variable bool", codigo3)

# Prueba 4: Asignación y suma
codigo4 = "let x = x + 1;"
mostrar_prueba("Prueba 4: Asignación y suma", codigo4)

# Prueba 5: Operadores relacionales
codigo5 = "if x >= 10 goto etiqueta;"
mostrar_prueba("Prueba 5: Operadores relacionales", codigo5)

# Prueba 6: Condicional completo
codigo6 = "if x == 1 goto a; else goto b;"
mostrar_prueba("Prueba 6: Condicional completo", codigo6)

# Prueba 7: Uso de not, and, or
codigo7 = "let b = not a and c or d;"
mostrar_prueba("Prueba 7: Uso de not, and, or", codigo7)

# Prueba 8: Goto
codigo8 = "goto fin;"
mostrar_prueba("Prueba 8: Goto", codigo8)

# Prueba 9: Paréntesis y rango
codigo9 = "(1...10)"
mostrar_prueba("Prueba 9: Paréntesis y rango", codigo9)

# Prueba 10: Error léxico
codigo10 = "let x = @;"
mostrar_prueba("Prueba 10: Error léxico", codigo10)

# Prueba 11: Dos puntos y punto
codigo11 = "var x : int."
mostrar_prueba("Prueba 11: Dos puntos y punto", codigo11)

# Prueba 12: Asignación extendida (:=)
codigo12 = "x := 42;"
mostrar_prueba("Prueba 12: Asignación extendida", codigo12)

# Prueba 13: Todos los operadores relacionales
codigo13 = "a < b > c <= d >= e == f <> g;"
mostrar_prueba("Prueba 13: Todos los REL_OP", codigo13)

# Prueba 14: Todos los operadores matemáticos
codigo14 = "x + y - z * w;"
mostrar_prueba("Prueba 14: Todos los MATH_OP", codigo14)

# Prueba 15: Paréntesis y punto y coma
codigo15 = "( x ) ;"
mostrar_prueba("Prueba 15: Paréntesis y punto y coma", codigo15)

# Prueba 16: Rango
codigo16 = "1...10"
mostrar_prueba("Prueba 16: Rango", codigo16)

# Prueba 17: Palabras reservadas todas juntas
codigo17 = "program var int bool true false begin end if else not and or goto let"
mostrar_prueba("Prueba 17: Todas las palabras reservadas", codigo17)

# Prueba 18: Espacios, tabs y saltos de línea
codigo18 = "a \t b \n c"
mostrar_prueba("Prueba 18: Espacios, tabs y saltos de línea", codigo18.replace("\\t", "\t").replace("\\n", "\n"))

# Prueba 19: Identificadores y números
codigo19 = "_id1 var2 12345"
mostrar_prueba("Prueba 19: Identificadores y números", codigo19)

# Prueba 20: Combinación de todo
codigo20 = "program test: begin let x := 1 + 2 * 3; if x >= 10 goto fin; end"
mostrar_prueba("Prueba 20: Combinación de todo", codigo20)

