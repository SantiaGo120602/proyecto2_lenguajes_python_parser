#!/bin/bash
export CLASSPATH=".:/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH"
alias antlr4='java -jar /usr/local/lib/antlr-4.11.1-complete.jar'
alias grun='java org.antlr.v4.gui.TestRig'

antlr4 -Dlanguage=Python3 python_grammar.g4
python3 main.py ejemplos/example.py
rm -v !("main.py"|"python_grammar.g4")