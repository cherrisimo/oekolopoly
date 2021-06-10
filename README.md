## gym-oekolopoly [![Python 3.9](https://img.shields.io/badge/python-3.9-blue)](https://img.shields.io/badge/python-3.9-blue)

Dieses Projekt basiert sich auf dem kybernetischen Spiel Ökolopoly entwickelt von Frederic Vester und veröffentlicht in 1983. 

Das Oekolopoly Environment benutzt diskrete Observation und Action Spaces und stellt eine vereinfachte Version des Spiels mit einem Startzustand und folgenden Funktionen zur Verfügung:
- [x] Verteilung von Aktionspunkten auf die erlaubten 5 Bereiche
- [x] Genaue Abbildung der Wirkungsgefüge für jeden Bereich
- [x] Berechnung von Aktionspunkten am Ende jeder Runde
- [x] Berechnung von Bilanz am Ende des Spiels


## Dependencies
```
conda install git
conda install pip
pip install gym
pip install PyQt5
```

## Installation
### Clonen mit SSH Link
```
git clone #SSH Link eingeben
cd oekolopoly
pip install -e .
```

### Clonen via GitHub Desktop 
```
cd oekolopoly
pip install -e .
```

## Use Cases
### Das Projekt via Command Prompt öffnen
#### Use Case 1: UI starten
```
python oekolopoly-gui/oeko_gui.py
```

#### Use Case 2: Tests starten
```
python oekolopoly/envs/tests.py
```

### Das Projekt via Spyder, bzw. andere IDEs öffnen
Die Dateien oeko_gui.py, oeko_env.py, tests.py immer von einer neuen Konsole laufen lassen.
