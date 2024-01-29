import numpy as np
import nazca as nd
from Optical_Components.LayerDeff import *






class StrWG:
    '''
    Straight Waveguide
    '''
    cell_name = "StrWG"

    def __init__(self, width_WG, length_WG, layer_Struct=Layer.Struct, layer_text_Pots = Layer.TXT_Ports, layer_Arrow = Layer.ARROW_CLR):
        '''
        

        Parameters
        ----------
        width_WG : int/float
            Width of the Waveguide.
        length_WG : int/float
            Length of the waveguide.
        layer_Struct : list, optional
            Layers Definition, do not change! The default is Layer.Struct.
        layer_text_Pots : list, optional
            Layers Definition, do not change! The default is Layer.TXT_Ports.
        layer_Arrow : list, optional
            Layers Definition, do not change! The default is Layer.ARROW_CLR.

        Returns
        -------
        None.

        '''

        self.width_WG = width_WG
        self.length_WG = length_WG
        self.layer_Struct = layer_Struct
        self.layer_text_Pots = layer_text_Pots
        self.layer_Arrow = layer_Arrow
 


        # create cell
        self._cell = self.create_gds()

    def create_gds(self):
        '''
        

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.

        '''
        with nd.Cell(StrWG.cell_name) as cell:
            cell_WG = [(0, self.width_WG / 2), (self.length_WG / 2, self.width_WG / 2),(self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, self.width_WG / 2), (0, self.width_WG / 2)]
            WG_1 = nd.Polygon(points=cell_WG, layer=self.layer_Struct).put(0, 0, 0)

            # cell_body = geom.box(length=self.length_WG, width=self.width_WG)
            # nd.Polygon(points=cell_body, layer=self.layer_Struct).put()

            nd.Pin(name = 'a0', width=self.width_WG).put(-self.length_WG/2, 0, 180)
            nd.Pin(name = 'b0', width=self.width_WG).put(self.length_WG/2, 0, 0)
            nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)

        return cell
    
    def put(self, *args, **kwargs):
        '''
        

        Parameters
        ----------
        *args : TYPE
            DESCRIPTION.
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        Cell to put on the nazca GDSII file
            Do not chnage.

        '''
        return self._cell.put(*args, **kwargs)
    





class StrWG_P2P:
    '''
    Straight Waveguide define from Pin to Pin
    '''
    cell_name = "StrWG_P2P"

    def __init__(self, pin1 , pin2, layer_Struct=Layer.Struct, layer_text_Pots = Layer.TXT_Ports, layer_Arrow = Layer.ARROW_CLR):
        '''
        

        arameters
        ----------
        pin1 : list of str
            List of str with the pin name. For example Struct.pin["SBendBezR_In"]
        pin2 : list of str
            List of str with the pin name. For example Struct.pin["SBendBezR_Out"]
        layer_Struct : TYPE, optional
            Layers Definition, do not change! The default is Layer.Struct.
        layer_text_Pots : list, optional
            Layers Definition, do not change! The default is Layer.TXT_Ports.
        layer_Arrow : list, optional
            Layers Definition, do not change! The default is Layer.ARROW_CLR.

        Returns
        -------
        None.

        '''
        self.pin1 = pin1
        self.pin2 = pin2
        self.layer_Struct = layer_Struct
        self.width_WG = self.pin1.width
        self.layer_text_Pots = layer_text_Pots
        self.layer_Arrow = layer_Arrow

        # create cell
        self._cell = self.create_gds_pin_to_pin()
    
    def create_gds_pin_to_pin(self):
        '''
        

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.

        '''
        with nd.Cell(StrWG.cell_name) as cell:
            # cell_body = geom.box(length=self.length_WG, width=self.width_WG)

            # connect them
            x1, y1, a1 = self.pin1.xya()
            x2, y2, a2 = self.pin2.xya()
            length = x1 - x2
            
            waveguide = nd.strt(width=self.width_WG, length=length, layer=self.layer_Struct).put()
            nd.Pin("a0", pin=waveguide.pin["a0"]).put()
            nd.Pin("b0", pin=waveguide.pin["b0"]).put()
            nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)

        return cell


    def put(self, *args, **kwargs):
        '''
        

        Parameters
        ----------
        *args : TYPE
            DESCRIPTION.
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        Cell to put on the nazca GDSII file
            Do not chnage.

        '''
        return self._cell.put(self.pin1, *args, **kwargs)