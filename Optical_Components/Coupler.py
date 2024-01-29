import numpy as np
import nazca as nd
from Optical_Components.LayerDeff import *
from Optical_Components.S_Bends import *






class MMI1x2:
    '''
    1x2 MMI GDS Class
    '''
    cell_name = "MMI1x2"
    def __init__(self,width_MMI, length_MMI, width_WG, length_WG, gap, layer_Struct= Layer.Struct, layer_text_Pots = Layer.TXT_Ports, layer_Arrow = Layer.ARROW_CLR , spacing = None, lenght_bend = None, pins = True):
        '''
        

        Parameters
        ----------
        width_MMI : int/float
            Width of the MMI.
        length_MMI : int/float
            Length of the MMI.
        width_WG : int/float
            Width of the Waveguide.
        length_WG : int/float
            Length of the Waveguide.
        gap : int/float
            Gap between the output Waveguides.
        layer_Struct : layer lib parametes, optional
            The default is Layer.Struct.
        layer_text_Pots : layer lib parametes, optional
            The default is Layer.Struct. The default is Layer.TXT_Ports.
        layer_Arrow : layer lib parametes, optional
            The default is Layer.Struct. The default is Layer.ARROW_CLR.
        spacing : int/float, optional
            Space between the Outputs of the Waveguides when S-Bends are used. The default is None.
        lenght_bend : int/float, optional
            Length of the S-Bends. The default is None.
        pins : boolen, optional
            Show pins in the GDSII file. The default is True.

        Returns
        -------
        None.

        '''
        self.width_MMI = width_MMI
        self.length_MMI = length_MMI
        self.width_WG = width_WG
        self.length_WG = length_WG
        self.gap = gap
        self.pins = pins
        self.layer_Struct = layer_Struct
        self.layer_text_Pots = layer_text_Pots
        self.layer_Arrow = layer_Arrow
        self.spacing = spacing
        self.lenght_bend = lenght_bend


        # create cell
        self._cell = self.create_gds()

    def create_gds(self):
        '''
        

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.

        '''
        with nd.Cell(MMI1x2.cell_name) as cell:
            if self.spacing:

                # calculate spacing and gap difference
                space = self.spacing/2 

                # Create the body and outputs of the 1x2 MMI
                cell_MMI_Body = [(0, self.width_MMI / 2), (self.length_MMI / 2, self.width_MMI / 2),(self.length_MMI / 2, -self.width_MMI / 2),(-self.length_MMI / 2, -self.width_MMI / 2),(-self.length_MMI / 2, self.width_MMI / 2), (0, self.width_MMI / 2)]
                nd.Polygon(points=cell_MMI_Body, layer=self.layer_Struct).put(0)

                cell_WG_In = [(0, self.width_WG / 2), (self.length_WG / 2, self.width_WG / 2),(self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, self.width_WG / 2), (0, self.width_WG / 2)]
                nd.Polygon(points=cell_WG_In, layer=self.layer_Struct).put(-self.length_MMI / 2 - self.length_WG/2, 0, 0)

                cell_WG_Out_Top = [(0, self.width_WG / 2), (self.length_WG / 2, self.width_WG / 2),(self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, self.width_WG / 2), (0, self.width_WG / 2)]
                nd.Polygon(points=cell_WG_Out_Top, layer=self.layer_Struct).put(self.length_MMI/2 + self.length_WG/2, self.width_WG/2 + self.gap/2, 0)

                cell_WG_Out_Bot = [(0, self.width_WG / 2), (self.length_WG / 2, self.width_WG / 2),(self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, self.width_WG / 2), (0, self.width_WG / 2)]
                nd.Polygon(points=cell_WG_Out_Bot, layer=self.layer_Struct).put(self.length_MMI/2 + self.length_WG/2, -self.width_WG/2 -self.gap/2, 0)


                # create the S-Bends 
                SBend_Top = SBends_Bezier(width_WG = self.width_WG, Bend_Length = self.lenght_bend, Offset = space, reverse = 1, pins=False).put(self.length_MMI/2 + self.length_WG,  -self.width_WG/2 - self.gap/2 - space/2, 0)
                SBend_Bot = SBends_Bezier(width_WG = self.width_WG, Bend_Length = self.lenght_bend, Offset = space, pins=False).put(self.length_MMI/2 + self.length_WG,  self.width_WG/2 + self.gap/2 + space/2, 0)
                

                if self.pins == True:
                    nd.Pin('MMI_In', width=self.width_WG).put(-self.length_MMI/2-self.length_WG, 0, 180)
                    nd.Pin('MMI_Out_Top', width=self.width_WG).put(self.length_MMI/2+self.length_WG + self.lenght_bend, space+self.width_WG/2 + self.gap/2, 0)
                    nd.Pin('MMI_Out_Bot', width=self.width_WG).put(self.length_MMI/2+self.length_WG + self.lenght_bend, -space-self.width_WG/2 -self.gap/2 , 0)
                    nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)
                else:
                    nd.put_stub()



            else:
                
                 # Create the body and outputs of the 1x2 MMI
                cell_MMI_Body = [(0, self.width_MMI / 2), (self.length_MMI / 2, self.width_MMI / 2),(self.length_MMI / 2, -self.width_MMI / 2),(-self.length_MMI / 2, -self.width_MMI / 2),(-self.length_MMI / 2, self.width_MMI / 2), (0, self.width_MMI / 2)]
                nd.Polygon(points=cell_MMI_Body, layer=self.layer_Struct).put(0)

                cell_WG_In = [(0, self.width_WG / 2), (self.length_WG / 2, self.width_WG / 2),(self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, self.width_WG / 2), (0, self.width_WG / 2)]
                nd.Polygon(points=cell_WG_In, layer=self.layer_Struct).put(-self.length_MMI / 2 - self.length_WG/2, 0, 0)

                cell_WG_Out_Top = [(0, self.width_WG / 2), (self.length_WG / 2, self.width_WG / 2),(self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, self.width_WG / 2), (0, self.width_WG / 2)]
                nd.Polygon(points=cell_WG_Out_Top, layer=self.layer_Struct).put(self.length_MMI/2 + self.length_WG/2, self.width_WG/2 + self.gap/2, 0)

                cell_WG_Out_Bot = [(0, self.width_WG / 2), (self.length_WG / 2, self.width_WG / 2),(self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, self.width_WG / 2), (0, self.width_WG / 2)]
                nd.Polygon(points=cell_WG_Out_Bot, layer=self.layer_Struct).put(self.length_MMI/2 + self.length_WG/2, -self.width_WG/2 -self.gap/2, 0)

                if self.pins == True:
                    nd.Pin('MMI_In', width=self.width_WG).put(-self.length_MMI/2-self.length_WG, 0, 180)
                    nd.Pin('MMI_Out_Top', width=self.width_WG).put(self.length_MMI/2+self.length_WG, self.width_WG/2 + self.gap/2, 0)
                    nd.Pin('MMI_Out_Bot', width=self.width_WG).put(self.length_MMI/2+self.length_WG, -self.width_WG/2 -self.gap/2, 0)
                    nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)
                else:
                    nd.put_stub()


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











class DirectionalCoupler:
    '''
    Directional Coupler
    '''
    cell_name = "DirectionalCoupler"
    def __init__(self, length_DC, width_WG, gap, layer_Struct=Layer.Struct, layer_text_Pots = Layer.TXT_Ports, layer_Arrow = Layer.ARROW_CLR, spacing = None, lenght_bend = None, pins = True):
        '''
        

        Parameters
        ----------
        length_DC : int/float
            Length of the Directional Coupler.
        width_WG : int/float
            Width of the Directional Coupler.
        gap : int/float
            Space between the waveguides of the Directional Coupler.
        layer_Struct : list, optional
            Layers Definition, do not change! The default is Layer.Struct.
        layer_text_Pots : list, optional
            Layers Definition, do not change! The default is Layer.TXT_Ports.
        layer_Arrow : list, optional
           Layers Definition, do not change! The default is Layer.ARROW_CLR.
        spacing : int/float, optional
            Space between the output and input waveguides after the S-Bends. The default is None.
        lenght_bend : int/float, optional
            Length of the S-Bends. The default is None.
        pins : boolen, optional
            Pins will be set on the GDSII file. The default is True.

        Returns
        -------
        None.

        '''
        self.length_DC = length_DC
        self.width_WG = width_WG
        self.gap = gap
        self.pins = pins
        self.layer_Struct = layer_Struct
        self.layer_text_Pots = layer_text_Pots
        self.layer_Arrow = layer_Arrow
        self.spacing = spacing
        self.lenght_bend = lenght_bend


        # create cell
        self._cell = self.create_gds()

    def create_gds(self):
        '''
        

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.


        '''
        with nd.Cell(DirectionalCoupler.cell_name) as cell:
            

            # calculate spacing and gap difference
            space = self.spacing + self.gap
            gap =  self.gap /2 +self.width_WG/2

            # create the body of the Directional Coupler
            cell_WG_Top = [(0, self.width_WG / 2), (self.length_DC / 2, self.width_WG / 2),(self.length_DC / 2, -self.width_WG / 2),(-self.length_DC / 2, -self.width_WG / 2),(-self.length_DC / 2, self.width_WG / 2), (0, self.width_WG / 2)]
            nd.Polygon(points= cell_WG_Top, layer=self.layer_Struct).put(0, gap, 0)

            cell_WG_Out_Bot = [(0, self.width_WG / 2), (self.length_DC / 2, self.width_WG / 2),(self.length_DC / 2, -self.width_WG / 2),(-self.length_DC / 2, -self.width_WG / 2),(-self.length_DC / 2, self.width_WG / 2), (0, self.width_WG / 2)]
            nd.Polygon(points= cell_WG_Out_Bot, layer=self.layer_Struct).put(0, -gap, 0)


            # create the S-Bends 
            Y_Offset = space/2 + gap
            X_Offset = self.length_DC / 2 + self.lenght_bend
            SBend_In_Top = SBends_Bezier(width_WG = self.width_WG, Bend_Length = self.lenght_bend, Offset = space, reverse = 1, pins=False).put(-X_Offset, Y_Offset, 0)
            SBend_In_Bot = SBends_Bezier(width_WG = self.width_WG, Bend_Length = self.lenght_bend, Offset = space, pins=False).put(-X_Offset, -Y_Offset, 0)
            SBend_Out_Top = SBends_Bezier(width_WG = self.width_WG, Bend_Length = self.lenght_bend, Offset = space, reverse = 1, pins=False).put(self.length_DC / 2, -Y_Offset, 0)
            SBend_Out_Bot = SBends_Bezier(width_WG = self.width_WG, Bend_Length = self.lenght_bend, Offset = space, pins=False).put(self.length_DC / 2, Y_Offset, 0)
            

            if self.pins == True:
                nd.Pin('DC_In_Top', width=self.width_WG).put(X_Offset, space + gap, 0)
                nd.Pin('DC_Out_Top', width=self.width_WG).put(-X_Offset, space + gap, 180)
                nd.Pin('DC_In_Bot', width=self.width_WG).put(X_Offset, -(space + gap) , 0)
                nd.Pin('DC_Out_Bot', width=self.width_WG).put(-X_Offset, -(space + gap), 180)
                nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)
            else:
                nd.put_stub()


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
    



class YJunction:
    '''
    Y-Junction
    '''
    cell_name = "YJunction"
    number = 0  

    def __init__(self, width_WG, length, gap, layer_Struct=Layer.Struct,  layer_text_Pots = Layer.TXT_Ports, layer_Arrow = Layer.ARROW_CLR ,spacing=None, Bend_Length = None, reverse = None):
        '''
        

        Parameters
        ----------
        width_WG : int/float
            Width of the Waveguide
        length : int/float
            Length of the Y-Junction
        gap : int/float
            Gap between the Output Wavguides.
        layer_Struct : list, optional
            Layers Definition, do not change! The default is Layer.Struct.
        layer_text_Pots : list, optional
            Layers Definition, do not change! The default is Layer.TXT_Ports.
        layer_Arrow : list, optional
            Layers Definition, do not change! The default is Layer.ARROW_CLR.
        spacing : int/float, optional
            Space between the Output Waveguides when S-Bends are used. The default is None.
        Bend_Length : int/float, optional
            Length of the S-Bends. The default is None.
        reverse : int/float, optional
            Set revers to an  random numbe, for example reverse = 1 to mirror the
            curve on the Y-Axis. The default is None.

        Returns
        -------
        None.

        '''
        self.width_WG = width_WG
        self.length = length
        self.gap = gap
        self.layer_Struct = layer_Struct
        self.layer_text_Pots = layer_text_Pots
        self.layer_Arrow = layer_Arrow
        self.spacing = spacing
        self.Bend_Length = Bend_Length
        self.reverse = reverse
        # radius = 50
        # self.radius = radius

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        '''
        

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.

        '''
        if self.reverse:    
            with nd.Cell(name=YJunction.cell_name) as cell:
                

                # if self.spacing:
                #     bend = SBendEuler(self.waveguide_width, waveguide_xs=self.waveguide_xs, offset=(self.spacing - self.gap)/2, radius=self.radius)
                #     waveguide_output2 = bend.put(self.length, self.gap/2)
                #     waveguide_output1 = bend.put(self.length, -self.gap/2, flip=True)
                if self.spacing:
                    Offset = (self.spacing - self.gap)/2
                    waveguide = nd.taper(length=self.length, shift=self.gap/2, width1=self.width_WG, width2=self.width_WG, layer=self.layer_Struct)
                    waveguide_input = waveguide_output1 = waveguide.put(self.length/2, 0, 180)
                    waveguide_output2 = waveguide.put(self.length/2, 0, 180, flip=True)
                    X_Offset,y,a = waveguide_output1.pin["b0"].xya()
                    bend1 = SBends_Bezier(width_WG = self.width_WG, Bend_Length = self.Bend_Length, Offset = Offset, reverse = 1, pins=False).put(X_Offset- self.Bend_Length, (self.gap/2 + Offset/2))
                    bend2 = SBends_Bezier(width_WG = self.width_WG, Bend_Length = self.Bend_Length, Offset = Offset, pins=False).put(X_Offset- self.Bend_Length, -(self.gap/2 + Offset/2))
                    # create pin
                    nd.Pin('YJunctionR_In', pin=waveguide_input.pin["a0"]).put(self.length/2,0,0)
                    nd.Pin('YJunctionR_Out1', pin=waveguide_output1.pin["b0"]).put(-self.length/2 - self.Bend_Length, (self.spacing/2), 180)
                    nd.Pin('YJunctionR_Out2', pin=waveguide_output2.pin["b0"]).put(-self.length/2 - self.Bend_Length, -(self.spacing/2), 180)
                    nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)
                
                else:
                    waveguide = nd.taper(length=self.length, shift=self.gap/2, width1=self.width_WG, width2=self.width_WG, layer=self.layer_Struct)
                    waveguide_input = waveguide_output1 = waveguide.put(-self.length/2, 0, 180)
                    waveguide_output2 = waveguide.put(-self.length/2, 0, 180, flip=True)
                    # create pin
                    nd.Pin('YJunctionR_In', pin=waveguide_input.pin["a0"]).put()
                    nd.Pin('YJunctionR_Out1', pin=waveguide_output1.pin["b0"]).put()
                    nd.Pin('YJunctionR_Out2', pin=waveguide_output2.pin["b0"]).put()
                    nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)
            return cell
        

        else:
            with nd.Cell(name=YJunction.cell_name) as cell:
                

                # if self.spacing:
                #     bend = SBendEuler(self.waveguide_width, waveguide_xs=self.waveguide_xs, offset=(self.spacing - self.gap)/2, radius=self.radius)
                #     waveguide_output2 = bend.put(self.length, self.gap/2)
                #     waveguide_output1 = bend.put(self.length, -self.gap/2, flip=True)
                if self.spacing:
                    Offset = (self.spacing - self.gap)/2
                    waveguide = nd.taper(length=self.length, shift=self.gap/2, width1=self.width_WG, width2=self.width_WG, layer=self.layer_Struct)
                    waveguide_input = waveguide_output1 = waveguide.put(-self.length/2, 0, 0)
                    waveguide_output2 = waveguide.put(-self.length/2, 0, flip=True)

                    X_Offset,y,a = waveguide_output1.pin["b0"].xya()
                    bend1 = SBends_Bezier(width_WG = self.width_WG, Bend_Length = self.Bend_Length, Offset = Offset, pins=False).put(X_Offset, (self.gap/2 + Offset/2))
                    bend2 = SBends_Bezier(width_WG = self.width_WG, Bend_Length = self.Bend_Length, Offset = Offset, reverse = 1, pins=False).put(X_Offset, -(self.gap/2 + Offset/2))
                    # create pin
                    nd.Pin('YJunction_In', pin=waveguide_input.pin["a0"]).put()
                    nd.Pin('YJunction_Out1', pin=waveguide_output1.pin["b0"]).put(self.length/2 + self.Bend_Length, (self.spacing/2))
                    nd.Pin('YJunction_Out2', pin=waveguide_output2.pin["b0"]).put(self.length/2 + self.Bend_Length, -(self.spacing/2))
                    nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)
                else:
                    waveguide = nd.taper(length=self.length, shift=self.gap/2, width1=self.width_WG, width2=self.width_WG, layer=self.layer_Struct)
                    waveguide_input = waveguide_output1 = waveguide.put(-self.length/2, 0, 0)
                    waveguide_output2 = waveguide.put(-self.length/2, 0, flip=True)
                    # create pin
                    nd.Pin('YJunction_In', pin=waveguide_input.pin["a0"]).put()
                    nd.Pin('YJunction_Out1', pin=waveguide_output1.pin["b0"]).put()
                    nd.Pin('YJunction_Out2', pin=waveguide_output2.pin["b0"]).put()
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