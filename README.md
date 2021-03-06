# gym-oekolopoly [![Python 3.9](https://img.shields.io/badge/python-3.9-blue)](https://img.shields.io/badge/python-3.9-blue)

Das Projekt basiert sich auf dem kybernetischen Spiel Ökolopoly entwickelt von Frederic Vester und veröffentlicht in 1983. 

Das Oekolopoly Environment benutzt diskrete Observation und Action Spaces und stellt eine vereinfachte Version des Spiels mit einem Startzustand und folgenden Funktionen zur Verfügung:
- [x] Verteilung von Aktionspunkten auf die erlaubten 5 Bereiche
- [x] Genaue Abbildung von dem Wirkungsgefüge für jeden Bereich
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
#### Use Case 1: GUI starten
```
cd oekolopoly-gui
python oeko_gui.py
```

#### Use Case 2: Tests starten
```
python oekolopoly/envs/tests.py
```

### Das Projekt via Spyder, bzw. andere IDEs öffnen
In der [`__init__.py`](https://github.com/cherrisimo/oekolopoly/blob/main/oekolopoly/__init__.py) sind Codezeilen hinzugefügt, die das Environment aus dem Gym Register löschen, so dass es kein Pflicht ist, die Dateien oeko_gui.py, oeko_env.py, tests.py immer von einer neuen Konsole laufen zu lassen.

## Rechte
### GUI
- Template: res/Combinear/Combinear.qss
- Rechte für Benutzung des Templates: res/Combinear/License.txt
- Icons: https://icons8.com

