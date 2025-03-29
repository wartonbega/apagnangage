# PAGE officielle d' l'APAGNANGE

Voici un exemple compréhensif d'apagnangage

```apagnangage
CRARI factoriel recursif
CRARI AP = factoriel; AGN = compteur max
QUOIFEUR FAIT 
    GENRE AGN C'EST A FAIT
        FEUR AP
    BELECK
    AP * AGN DANS AP
    AGN A - DANS AGN
    FEUR QUOI ANAGNAP
BELECK DANS ANAGNAP
```

---
## Pour recompiler le langage

La définition du langage est dans [APAGNANGAGE.g4](./APAGNANGAGE.g4)

```bash
sudo apt install antlr4 # version 4.13.2
antlr4 -Dlanguage=Python3 APAGNANGAGE.g4 -visitor
```
