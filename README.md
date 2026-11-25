# devloop-sandbox

Repository di prova per installare [devloop](https://github.com/brushtyler/devloop) su un progetto
che non lo contiene (ADR 0006, R9; brushtyler/devloop#515). Il codice è volutamente minimo.

```bash
python3 -m unittest discover -s tests -v
```

Versioni di Python supportate: 3.12 e 3.13 (la CI esegue i test su entrambe).
