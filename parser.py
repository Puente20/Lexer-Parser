from lexer import lexer
gramatica = {'TCode':{'PROGRAM':['PROGRAM','ID','DOT','Body']},
             'Body':{'BEGIN':['BEGIN','StatementList','END'],
                     'VAR':['VAR','DecVar','DecVarList','BEGIN','StatementList','END']},
             'DecVarList':{'BEGIN':['DecVarList1'],
                           'ID':['DecVarList1']},
             'DecVarList1':{'ID':['DecVar','DecVarList1'],
                            'BEGIN':[]}, # Los SD son (lambda,begin), no tomo en cuenta lambda
             'DecVar':{'ID':['ID','COLON','DecVarBody']},
             'DecVarBody':{'INT':['INT','LPAREN','NUM','RANGE','NUM','RPAREN','ASSIGN','NUM','SEMIDOT'],
                           'BOOL':['BOOL','ASSIGN','DecVarBody1']},
             'DecVarBody1':{'TRUE':['TRUE','SEMIDOT'],
                            'FALSE':['FALSE','SEMIDOT']},
             'StatementList':{'ID':['StatementList1'],
                              'LET':['StatementList1'],
                              'GOTO':['StatementList1'],
                              'IF':['StatementList1'],
                              'END':['StatementList1']},
             'StatementList1':{
                              'ID':['Statement','StatementList1'],
                              'IF':['Statement','StatementList1'],
                              'GOTO':['Statement','StatementList1'],
                              'LET':['Statement','StatementList1'],
                              'END':[]},
             'Statement':{'ID':['ID','COLON','StatementBody'],
                          'LET':['StatementBody'],
                          'IF':['StatementBody'],
                          'GOTO':['StatementBody']},
             'StatementBody':{'LET':['Assignment'],
                              'IF':['Conditional'],
                              'GOTO':['Goto']},
             'Goto':{'GOTO':['GOTO','ID','SEMIDOT']},
             'Assignment':{'LET':['LET','Lvalue','ASSIGN','Assignment1']},
             'Assignment1':{'NOT':['NOT','Rvalue','SEMIDOT'],
                            'ID':['Rvalue','Assignment2'],
                            'NUM':['Rvalue','Assignment2'],
                            'TRUE':['Rvalue','Assignment2'],
                            'FALSE':['Rvalue','Assignment2']},
             'Assignment2':{'SEMIDOT':['SEMIDOT'],
                            'MATH_PLUS':['OP','Rvalue','SEMIDOT'],
                            'MATH_MINUS':['OP','Rvalue','SEMIDOT'],
                            'MATH_MULT':['OP','Rvalue','SEMIDOT'],
                            'OR':['OP','Rvalue','SEMIDOT'],
                            'AND':['OP','Rvalue','SEMIDOT'],},
             'OP':{'MATH_PLUS':['MATH_PLUS'],
                   'MATH_MINUS':['MATH_MINUS'],
                   'MATH_MULT':['MATH_MULT'],
                   'OR':['OR'],
                   'AND':['AND']},
             'MatOp':{'MATH_PLUS':['MATH_PLUS'],
                      'MATH_MINUS':['MATH_MINUS'],
                      'MATH_MULT':['MATH_MULT']},
             'BoolOp':{'OR':['OR'],
                       'AND':['AND']},
             'Lvalue':{'ID':['ID']},
             'Rvalue':{'ID':['ID'],
                        'NUM':['NUM'],
                        'TRUE':['TRUE'],
                        'FALSE':['FALSE']},
             'Conditional':{'IF':['IF','CompExpr','GOTO','ID','SEMIDOT','Conditional1']},
             'Conditional1':{'ELSE':['ELSE','GOTO','ID','SEMIDOT'],
                             'ID':[],
                             'LET':[],
                             'GOTO':[],
                             'IF':[],
                             'END':[]}, 
             'CompExpr':{'ID':['Rvalue','CompOp','Rvalue'],
                         'NUM':['Rvalue','CompOp','Rvalue'],
                         'TRUE':['Rvalue','CompOp','Rvalue'],
                         'FALSE':['Rvalue','CompOp','Rvalue']},
             'CompOp':{'REL_IG':['REL_IG'],
                       'REL_DIS':['REL_DIS'],
                       'REL_MEN':['REL_MEN'],
                       'REL_MAY':['REL_MAY'],
                       'REL_MENIG':['REL_MENIG'],
                       'REL_MAYIG':['REL_MAYIG']}   
}

def procesar(cuerpo_produccion, datos_locales):
    for simbolo in cuerpo_produccion:
        if simbolo == []:  
            return
        token_actual = datos_locales['tokens'][datos_locales['index']][0]
        datos_locales['error'] = False

        # Terminal
        if simbolo not in gramatica:
            if simbolo == token_actual:
                datos_locales['index'] += 1
                if simbolo != token_actual:
                    datos_locales['derivaciones'].append(f"{simbolo} -> {token_actual}")
            else:
                datos_locales['error'] = True
                return
        else:
            derivacion = f"{simbolo} -> {gramatica[simbolo][token_actual]}"
            if simbolo != gramatica[simbolo][token_actual]:
                datos_locales['derivaciones'].append(derivacion)
            procedimiento(simbolo, datos_locales)
            if datos_locales['error']:
                return

def procedimiento(no_terminal, datos_locales):
    token_actual = datos_locales['tokens'][datos_locales['index']][0]
    datos_locales['error'] = False

    if token_actual in gramatica[no_terminal]:
        cuerpo = gramatica[no_terminal][token_actual]
        procesar(cuerpo, datos_locales)
    else:
        datos_locales['error'] = True


def algoritmo_principal(codigo_fuente):
    datos_locales = {
        'tokens': codigo_fuente + [('Eof', 'Eof')],
        'index': 0,
        'error': False,
        'derivaciones': []  
    }

    procedimiento('TCode', datos_locales)
    token_actual = datos_locales['tokens'][datos_locales['index']][0]

    if not datos_locales['error'] and token_actual == 'Eof':
        print("La cadena pertenece al lenguaje")
        print("\nDerivación de la cadena:")
        for derivacion in datos_locales['derivaciones']:
            print(derivacion)
    else:
        print("La cadena NO pertenece al lenguaje")

def mostrar_prueba_parser(nombre, codigo):
    print(f"\n--- {nombre} ---")
    print("Entrada:")
    print(codigo)
    try:
        tokens = lexer(codigo) 
        print("Tokens generados:")
        for token in tokens:
            print(token)
        print("Resultado del parser:")
        algoritmo_principal(tokens)
    except Exception as e:
        print("Error:", e)

# PRUEBAS DEL PARSER

# Prueba 1: Programa mínimo válido
codigo1 = """program ejemplo.
begin
end"""
mostrar_prueba_parser("Prueba 1: Programa mínimo válido", codigo1)

# Prueba 2: Declaración de variable válida
codigo2 = """program ejemplo.
var x : int(1...20) = 10;
begin
end"""
mostrar_prueba_parser("Prueba 2: Declaración de variable válida", codigo2)

# Prueba 3: Condicional válido
codigo3 = """program ejemplo.
begin
if x > 5 goto etiqueta;
end"""
mostrar_prueba_parser("Prueba 3: Condicional válido", codigo3)

# Prueba 4: Uso de operadores booleanos
codigo4 = """program ejemplo.
begin
let b = a and c;
let d = a or c;
let e = not a;
end"""
mostrar_prueba_parser("Prueba 4: Uso de operadores booleanos", codigo4)

# Prueba 5: Goto válido
codigo5 = """program ejemplo.
begin
goto fin;
end"""
mostrar_prueba_parser("Prueba 5: Goto válido", codigo5)

# Prueba 6: Error léxico (carácter inválido)
codigo6 = """program ejemplo.
begin
let x = @;
end"""
mostrar_prueba_parser("Prueba 6: Error léxico (carácter inválido)", codigo6)

# Prueba 7: Error sintáctico (estructura inválida)
codigo7 = """program ejemplo.
begin
var x int = 10;
end"""
mostrar_prueba_parser("Prueba 7: Error sintáctico (estructura inválida)", codigo7)

# Prueba 8: Uso de rango válido
codigo8 = """program ejemplo.
var x : int(1...10) = 5;
begin
end"""
mostrar_prueba_parser("Prueba 8: Uso de rango válido", codigo8)

# Prueba 9: Operadores relacionales válidos
codigo9 = """program ejemplo.
begin
if x >= 10 goto etiqueta;
end"""
mostrar_prueba_parser("Prueba 9: Operadores relacionales válidos", codigo9)

# Prueba 10: Combinación de todo
codigo10 = """program test.
var x : int(1...20) = 10;
begin
let y = x + 5;
if y > 10 goto etiqueta;
end"""
mostrar_prueba_parser("Prueba 10: Combinación de todo", codigo10)





