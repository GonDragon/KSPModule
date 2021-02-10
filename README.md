# KSPModule

This proyect intends to create a python library to parse, analyze, modify and write cfg files for Kerbal Space Program. In first instance, it will only read common files, but the intention is to also make it capable of read, proces and write patches for module manager.

## Getting Started

### Prerequisites

TODO

### Installation

TODO

## Usage

The usage is fairly simple. First, import the Reader from the KSPModule in your script

```python
from KSPModule import Reader
```

Now you have to load the Reader. The reader will receive a file or a string, and will parse it.

```python
# Loading from a file
# it is recommended to use the decoder utf-8-sig
with open('file.cfg', 'r', encoding='utf-8-sig') as cfgFile:
    reader = Reader(cfgFile)


# Loading from a String
string = 'MODULE{\n  attribute = value\n}'
reader = Reader(string)
```

TODO Documentation
