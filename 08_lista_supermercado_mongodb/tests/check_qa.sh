#!/bin/bash

# Teste de cobertura de código
coverage erase

coverage run -m pytest

coverage report

coverage xml -o ../reports/coverage_report.xml

coverage html -d ../reports/converage_report_html

# Verificação de erros estático no código, além de incentiva bons padrões de codificação
pylint ../lista_supermercado_mongodb/ --output-format=parseable:../reports/lint_report.txt

pylint ../lista_supermercado_mongodb/ --output-format=json:../reports/lint_report.json

pylint-json2html -o ../reports/lint_report.html ../reports/lint_report.json