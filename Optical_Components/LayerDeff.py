import nazca as nd
from copy import deepcopy

# create table layer
layers = {
    "PAYLOAD": 0,
    "Struct": 11,
    "TXT_Struct": 12,
    "MET1": 41,
    "TXT_MET1": 42,
    "VIA": 51,
    "TXT_VIA": 52,
    "MET2": 61,
    "TXT_MET2": 62,
    "CLD_OPEN": 65,
    "DEEP_GRID": 71, 
    "TXT_DEEP_GRID":72,
    "ARROW_CLR":81,
    "TXT_Ports":82
}


# create class layer
class Layer:
    PAYLOAD = "PAYLOAD"
    Struct = "Struct"
    TXT_Struct = "TXT_Struct"
    MET1 = "MET1"
    TXT_MET1 = "TXT_MET1"
    VIA = "VIA"
    TXT_VIA = "TXT_VIA"
    MET2 = "MET2"
    TXT_MET2 = "TXT_MET2"
    CLD_OPEN = "CLD_OPEN"
    DEEP_GRID = "DEEP_GRID"
    TXT_DEEP_GRID = "TXT_DEEP_GRID"
    ARROW_CLR = "ARROW_CLR"
    TXT_Ports = "TXT_Ports"
    


# create the layer
for name, layer in layers.items():
    nd.add_layer(name=name, layer=layer)


# create table xs
xss = {
    "Struct": [{"layer": layers["Struct"]}],
    "TXT_Struct": [{"layer": layers["TXT_Struct"]}],
    "MET1": [{"layer": layers["MET1"]}],
    "TXT_MET1": [{"layer": layers["TXT_MET1"]}],
    "VIA": [{"layer": layers["VIA"]}],
    "TXT_VIA": [{"layer": layers["TXT_VIA"]}],
    "MET2": [{"layer": layers["MET2"]}],
    "TXT_MET2": [{"layer": layers["TXT_MET2"]}],
    "CLD_OPEN": [{"layer": layers["CLD_OPEN"]}],
    "DEEP_GRID": [{"layer": layers["DEEP_GRID"]}],
    "TXT_DEEP_GRID": [{"layer": layers["TXT_DEEP_GRID"]}],
    "ARROW_CLR": [{"layer": layers["ARROW_CLR"]}],
    "TXT_Ports": [{"layer": layers["TXT_Ports"]}]
}


# create class xs
class XS:
    Struct = "Struct"
    TXT_Struct = "TXT_Struct"
    MET1 = "MET1"
    TXT_MET1 = "TXT_MET1"
    VIA = "VIA"
    TXT_VIA = "TXT_VIA"
    MET2 = "MET2"
    TXT_MET2 = "TXT_MET2"
    CLD_OPEN = "CLD_OPEN"
    DEEP_GRID = "DEEP_GRID"
    TXT_DEEP_GRID = "TXT_DEEP_GRID"
    ARROW_CLR = "ARROW_CLR"
    TXT_Ports = "TXT_Ports"


# create the xs
for name, values in xss.items():
    for value in values:
        nd.add_layer2xsection(xsection=name, **value)
