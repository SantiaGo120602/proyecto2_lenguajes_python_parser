# proyecto2_lenguajes_python_parser

> En este repositorio se puede encontrar un analizador sintáctico para el lenguaje de progración Python, implementado en python-antlr4.

>**Prerrequisitos**:
* python3
* java 11 o superior
* antlr4 4.11.1
* antlr4-python3-runtime 4.11.1

>**Setup**:
Deben ejecutarse por consola las siguientes lineas de comandos:
```bash
export CLASSPATH=".:/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"
alias antlr4='java -jar /usr/local/lib/antlr-4.11.1-complete.jar'
alias grun='java org.antlr.v4.gui.TestRig'
```
>Ejecución:
Para usar el analizador sintáctico existen dos maneras:
* Ingresar a la linea de comandos del analizador:
```python
python3 main.py
```
* Ingresar la ubicación de un archivo para ser analizado sintácticamente. En la carpeta ejemplos se encuentran algunos archivos en lenguaje python:
```python
python3 main.py ejemplos/example.py
```

>**Errores**:
Si se presenta algún error se puede recompilar el proyecto con las siguientes líneas de código:
```bash
antlr4 -Dlanguage=Python3 python_grammar.g4
rm -v !("main.py"|"python_grammar.g4")
```
