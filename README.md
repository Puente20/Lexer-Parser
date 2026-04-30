# Lexer-Parser

# Analizador Lexicografico y Sintactico - Lenguaje TINY

Este proyecto consiste en el desarrollo de un compilador (Lexer y Parser) para el lenguaje TINY. Fue realizado de forma grupal en un equipo de 4 integrantes.

# Objetivo

Crear e Implementar un Analizador Lexicografico (Lexer) para el lenguaje de programacion TINY, cuya gramatica se especifica posteriormente.

El software resultante de la implementacion del lexer aceptara como entrada una cadena que representa codigo escrito en el lenguaje TINY, y debera convertir este codigo, interpretado como una secuencia de caracteres ASCII o UTF-8, a una lista de tokens correspondiente a la gramatica provista. Cada token estara representado por un par (tipo_token, lexema), donde el tipo representa la clasificacion y el lexema es el valor asociado.

## Especificación de la gramática

VN = {T Code, Body, DecVarList, DecVar, DecVarBody, Statement, StatementList, StatementBody,
Goto, Assingment, Op, MatOp, BoolOp, Lvalue, Rvalue, Conditional, CompExpr, CompOp}
VT = {id, num, program, var, . , ; , =, :=, int, bool, true, f alse, begin, end, if, else,
not, <, >, <>, <=, >=, +, −, ∗, ==, (, ), · · · , and, or}
S = T Code

## Producciones

P = {T Code −→ program id . Body
Body −→ begin StatementList end
| var DecVar DecVarList begin StatementList end
DecV arList −→ DecVarList DecV ar
| λ
DecVar −→ id : DecVarBody
DecVarBody −→ int ( num · · · num ) = num ;
| bool = true ;
| bool = false ;
StatementList −→ StatementList Statement
| λ
Statement −→ id : StatementBody
| StatementBody
StatementBody −→ Assignment
| Conditional
| Goto
Goto −→ goto id ;
Assignment −→ let Lvalue = Rvalue ;
| let Lvalue = Rvalue Op Rvalue ;
| let Lvalue = not Rvalue ;
Op −→ MatOp
| BoolOp
MatOp −→ +
| -
| *
BoolOp −→ or
| and
Lvalue −→ id
Rvalue −→ id
| num
| true
| false
Conditional −→ if CompExpr goto id ; else goto id ;
| if CompExpr goto id ;
CompExpre −→ Rvalue CompOp Rvalue
CompOp −→ ==
| <>
| <
| >
| <=
| >=
}

# Estructura del proyecto

- lexer.py: Contiene los Automatas Finitos Deterministicos (AFD) para la identificacion de tokens.  

- parser.py: Implementa el analisis sintactico descendente basado en la gramatica provista.

# Integrantes

1. Tomas Puente de la Fuente
2. Andres Fonseca
3. Tomas Vera
4. Martin Aristia
