import numpy as np
import nazca as nd
from LayerDeff import *
import nazca.geometries as geom





class MMI1x2:
    '''
    1x2 MMI GDS Class
    '''
    cell_name = "MMI1x2"
    def __init__(self,width_MMI, length_MMI, width_WG, length_WG, gap, layer_Struct=Layer.Struct, spacing = None, lenght_bend = None, pins = True):
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
        spacing : int/float, optional
            This is an optional parameter and it set the sapce between the output Waveguides when S-Bends are used. The default is None. 
        lenght_bend : int/float, optional
            Length of the S-Bend. The default is None.
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
                # space = self.spacing/2 + self.gap/2  #+ self.width_WG / 2
                space = self.spacing/2 

                #create the MMI
                # cell_io = geom.box(length=self.length_WG, width=self.width_WG)
                # cell_body = geom.box(length=self.length_MMI, width=self.width_MMI)
                # nd.Polygon(points=cell_io, layer=self.layer_Struct).put(-self.length_WG-self.length_MMI/2, 0, 0)
                # nd.Polygon(points=cell_body, layer=self.layer_Struct).put(-self.length_MMI / 2, 0, 0)
                # nd.Polygon(points=cell_io, layer=self.layer_Struct).put(self.length_MMI/2, self.width_WG/2 + self.gap/2, 0)
                # nd.Polygon(points=cell_io, layer=self.layer_Struct).put(self.length_MMI/2, -self.width_WG/2 -self.gap/2, 0)

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
                    nd.put_stub()
                else:
                    nd.put_stub()



            else:
                # cell_io = geom.box(length=self.length_WG, width=self.width_WG)
                # cell_body = geom.box(length=self.length_MMI, width=self.width_MMI)

                # nd.Polygon(points=cell_io, layer=self.layer_Struct).put(-self.length_WG-self.length_MMI/2, 0, 0)
                # nd.Polygon(points=cell_body, layer=self.layer_Struct).put(-self.length_MMI / 2, 0, 0)
                # nd.Polygon(points=cell_io, layer=self.layer_Struct).put(self.length_MMI/2, self.width_WG/2 + self.gap/2, 0)
                # nd.Polygon(points=cell_io, layer=self.layer_Struct).put(self.length_MMI/2, -self.width_WG/2 -self.gap/2, 0)

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
                    nd.put_stub()
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





# parameters = {"width_MMI":40, "length_MMI":50, "width_WG":2, "length_WG":10, "gap":10, "spacing": 25, "lenght_bend": 10}
# MMi1 = MMI1x2(**parameters).put(0,0,0)

# nd.export_gds()




class StrWG:
    '''
    Straight Waveguide
    '''
    cell_name = "StrWG"

    def __init__(self, width_WG, length_WG, layer_Struct=Layer.Struct):
        '''
        

        Parameters
        ----------
        width_WG : int/float
            Width of the Waveguide.
        length_WG : int/float
            Length of the waveguide.
        layer_Struct : list, optional
            Layers Definition, do not change! The default is Layer.Struct.

        Returns
        -------
        None.

        '''

        self.width_WG = width_WG
        self.length_WG = length_WG
        self.layer_Struct = layer_Struct
 


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

            nd.Pin('a0', width=self.width_WG).put(-self.length_WG/2, 0, 180)
            nd.Pin('b0', width=self.width_WG).put(self.length_WG/2, 0, 0)
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
    





class StrWG_P2P:
    '''
    Straight Waveguide define from Pin to Pin
    '''
    cell_name = "StrWG_P2P"

    def __init__(self, pin1 , pin2, layer_Struct=Layer.Struct ):
        '''
        

        Parameters
        ----------
        pin1 : list of str
            List of str with the pin name. For example Struct.pin["SBendBezR_In"]
        pin2 : list of str
            List of str with the pin name. For example Struct.pin["SBendBezR_Out"]
        layer_Struct : TYPE, optional
            DESCRIPTION. The default is Layer.Struct.

        Returns
        -------
        None.

        '''
        self.pin1 = pin1
        self.pin2 = pin2
        self.layer_Struct = layer_Struct
        self.width_WG = self.pin1.width


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
        return self._cell.put(self.pin1, *args, **kwargs)
        

    





class SBends_Bezier:
    '''
    S-Bends Bezier
    '''
    cell_name = "SBends_Bezier"

    def __init__(self, width_WG, Bend_Length, Offset, layer_Struct=Layer.Struct, reverse = None, pins = True):
        '''
        

        Parameters
        ----------
        width_WG : int/float
            Width of Waveguide.
        Bend_Length : int/float
            Length of S-Bend.
        Offset : int/float
            Input to Output offset.
        layer_Struct : list, optional
            Layers Definition, do not change! The default is Layer.Struct.
        reverse : int/float, optional
            Set revers to an  random numbe, for example reverse = 1 to mirror the
            curve on the Y-Axis. The default is None.
        pins : boolen, optional
            Show pins in the GDSII file. The default is True.
         : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.width_WG = width_WG
        self.Bend_Length = Bend_Length
        self.Offset = Offset
        self.layer_Struct=layer_Struct
        self.reverse = reverse
        self.pins = pins
        self.arr = []


        # create cell
        self._cell = self.create_gds()


     
    def create_gds(self):
        '''
        

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.

        '''
        with nd.Cell(SBends_Bezier.cell_name) as cell:
            if self.reverse:
                def x(t, x_S, **kwargs):
                    """X as function of t and free parameters."""
                    return (1-t)**3*0 + 3*(1-t)**2*t*x_S/2 + 3*(1-t)*t**2*x_S/2 + t**3*x_S
                def y(t, y_S, **kwargs):
                    """Y as function of t and free parameters."""
                    return -((1-t**3)*0 + 3*(1-t)**2*t*0 + 3*(1-t)*t**2*y_S + t**3*y_S)
                def w(t, width=None, **kwargs):
                    """Width (constant)."""
                    return width
                # include defaults for *all* free parameters used in the functions x, y and w.
                params = {'x_S':self.Bend_Length, 'y_S':self.Offset, 'width':self.width_WG} 
                S_bend_bot = nd.Tp_viper(x= x, y= y, w= w, N=100 , layer = self.layer_Struct, **params)
                S_bend_bot(width1=1.0).put(0, self.Offset/2, 0)
                if self.pins == True:
                    nd.Pin('SBendBezR_In', width=self.width_WG).put(0, self.Offset/2, 180)
                    nd.Pin('SBendBezR_Out', width=self.width_WG).put(self.Bend_Length, -self.Offset/2, 0)
                    nd.put_stub()
                else:
                    nd.put_stub()


            else:
                def x(t, x_S, **kwargs):
                    """X as function of t and free parameters."""
                    return (1-t)**3*0 + 3*(1-t)**2*t*x_S/2 + 3*(1-t)*t**2*x_S/2 + t**3*x_S
                def y(t, y_S, **kwargs):
                    """Y as function of t and free parameters."""
                    return (1-t**3)*0 + 3*(1-t)**2*t*0 + 3*(1-t)*t**2*y_S + t**3*y_S
                def w(t, width=None, **kwargs):
                    """Width (constant)."""
                    return width
                # include defaults for *all* free parameters used in the functions x, y and w.
                params = {'x_S':self.Bend_Length, 'y_S':self.Offset, 'width':self.width_WG} 
                S_bend_bot = nd.Tp_viper(x= x, y= y, w= w, N=100 , layer = self.layer_Struct, **params)
                S_bend_bot(width1=1.0).put(0, -self.Offset/2, 0)
                if self.pins == True:
                    nd.Pin('SBendBez_In', width=self.width_WG).put(0, -self.Offset/2, 180)
                    nd.Pin('SBendBez_Out', width=self.width_WG).put(self.Bend_Length, self.Offset/2, 0)
                    nd.put_stub()
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
    








class SBends_Cos:
    '''
    S-Bend Cosinus Function
    '''
    cell_name = "SBends_Cos"

    def __init__(self, width_WG, Bend_Length, Offset, layer_Struct=Layer.Struct, reverse = None):
        '''
        

        Parameters
        ----------
        width_WG : int/float
            Width Waveguide.
        Bend_Length : int/float
            Length of the S-Bend.
        Offset : int/float
            Input to Output offset.
        layer_Struct : list, optional
            Layers Definition, do not change! The default is Layer.Struct.
        reverse : int/float, optional
            Set revers to an  random numbe, for example reverse = 1 to mirror the
            curve on the Y-Axis. The default is None.

        Returns
        -------
        None.

        '''
        self.width_WG = width_WG
        self.Bend_Length = Bend_Length
        self.Offset = Offset
        self.layer_Struct = layer_Struct
        self.arr = []
        self.reverse = reverse

        # create cell
        self._cell = self.create_gds()

    def create_gds(self):
        '''
        

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.

        '''
        if self.reverse:
            with nd.Cell(SBends_Cos.cell_name) as cell:
                lenght = np.linspace(0,self.Bend_Length,1000)
                def testcurve( P, L):
                    t = np.linspace(0,L,1000)
                    y = P*(np.cos((np.pi/(2*L))*t)**2)
                    return y

                Curve = testcurve( self.Offset, self.Bend_Length)

                for i in range(len(lenght)):
                    self.arr.append((lenght[i],Curve[i]))

                points = self.arr 
                nd.Polyline(points=points, layer=self.layer_Struct, width = self.width_WG).put(0, -self.Offset/2, 0)
                nd.Pin('SBendCosR_In', width=self.width_WG).put(0, self.Offset/2, 180)
                nd.Pin('SBendCosR_Out', width=self.width_WG).put(self.Bend_Length, -self.Offset/2, 0)
                nd.put_stub()
            return cell
        
        else:
            with nd.Cell(SBends_Cos.cell_name) as cell:
                lenght = np.linspace(0,self.Bend_Length,1000)
                def testcurve( P, L):
                    t = np.linspace(0,L,1000)
                    y = P*(np.cos((np.pi/(2*L))*t)**2)
                    return y[::-1]

                Curve = testcurve( self.Offset, self.Bend_Length)

                for i in range(len(lenght)):
                    self.arr.append((lenght[i],Curve[i]))

                points = self.arr 
                nd.Polyline(points=points, layer=self.layer_Struct, width = self.width_WG).put(0, -self.Offset/2, 0)
                nd.Pin('SBendCos_In', width=self.width_WG).put(0, -self.Offset/2, 180)
                nd.Pin('SBendCos_Out', width=self.width_WG).put(self.Bend_Length, self.Offset/2, 0)
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





# parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2}
# SBend1 = SBends_Cos(**parameters).put(0,0,0)

# parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2, "reverse":1}
# SBend2 = SBends_Cos(**parameters).put(500,0,0)





# parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2}
# SBendB1 = SBends_Bezier(**parameters).put(0,0,0)
# # nd.export_plt()

# parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2, "reverse":1}
# SBendB2 = SBends_Bezier(**parameters).put(0,0,0)



# parameters = {"pin2": SBend1.pin["SBendCos_Out"], "pin1": SBend2.pin["SBendCosR_In"]}
# s1 = StrWG_P2P(**parameters).put(0,0,0) 

# parameters = {"pin2": SBendB1.pin["SBendBez_Out"], "pin1": SBendB2.pin["SBendBezR_In"]}
# s2 = StrWG_P2P(**parameters).put(0,0,0)

# nd.export_gds()



class Border:
    '''
    Set and Chip Frame to the GDSII File
    '''
    cell_name = "Border"
    text_offset_x = 150
    text_offset_y = 30


    def __init__(self, chip_size_x, chip_size_y, layer_deep_grid=Layer.DEEP_GRID, text_layer=Layer.TXT_Struct,layer_payload=Layer.PAYLOAD, layer_clad_open=Layer.CLD_OPEN, text_bottom = "", text_top = "" ):
        '''
        

        Parameters
        ----------
        chip_size_x : int/float
            Width of the Chip.
        chip_size_y : int/float
            Length of the Chip.
        layer_deep_grid : list, optional
            Layers Definition, do not change! The default is Layer.DEEP_GRID.
        text_layer :  list, optional
            Layers Definition, do not change! The default is Layer.TXT_Struct.
        layer_payload : list, optional
            Layers Definition, do not change! The default is Layer.PAYLOAD.
        layer_clad_open : list, optional
            Layers Definition, do not change! The default is Layer.CLD_OPEN.
        text_bottom : str, optional
            An Text that appears under the chip main Frame. The default is "".
        text_top : str, optional
            An Text that appears over the chip main Frame. The default is "".

        Returns
        -------
        None.

        '''
        self.chip_size_x = chip_size_x
        self.chip_size_y = chip_size_y
        self.layer_deep_grid = layer_deep_grid
        self.text_bottom = text_bottom
        self.text_top = text_top
        self.text_layer = text_layer
        self.layer_payload = layer_payload
        self.layer_clad_open = layer_clad_open
        self.extra_size = 150


        # calculate parameter
        self.border_x = self.chip_size_x / 2 
        self.border_y = self.chip_size_y / 2 
        self.full_size_x = self.extra_size + self.border_x
        self.full_size_y = self.extra_size + self.border_y
        self._cell = self.create_gds()

    def create_gds(self):
        '''
        

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.

        '''
        
        with nd.Cell(name=Border.cell_name) as cell:
            

            # add the boundary
            square_Chip = [(-self.border_x,  0), (-self.border_x, self.border_y), (self.border_x, self.border_y), (self.border_x, -self.border_y), (-self.border_x, -self.border_y), (-self.border_x, 0)]
            square_Edge_T = [(0,  self.full_size_y), (self.full_size_x, self.full_size_y), (self.full_size_x, self.border_y), (-self.full_size_x, self.border_y), (-self.full_size_x, self.full_size_y), (0, self.full_size_y)]
            square_Edge_B = [(0,  -self.full_size_y), (self.full_size_x, -self.full_size_y), (self.full_size_x, -self.border_y), (-self.full_size_x, -self.border_y), (-self.full_size_x, -self.full_size_y), (0, -self.full_size_y)]
            square_Edge_L = [(-self.full_size_x,  0), (-self.full_size_x, self.full_size_y), (-self.border_x, self.full_size_y), (-self.border_x, -self.full_size_y), (-self.full_size_x, -self.full_size_y), (-self.full_size_x, 0)]
            square_Edge_R = [(self.full_size_x,  0), (self.full_size_x, self.full_size_y), (self.border_x, self.full_size_y), (self.border_x, -self.full_size_y), (self.full_size_x, -self.full_size_y), (self.full_size_x, 0)]
            

            # add Polygons
            nd.Polygon(points=square_Chip , layer=self.layer_payload).put()
            nd.Polygon(points=square_Edge_T , layer=self.layer_deep_grid).put()
            nd.Polygon(points=square_Edge_B , layer=self.layer_deep_grid).put()
            nd.Polygon(points=square_Edge_L , layer=self.layer_deep_grid).put()
            nd.Polygon(points=square_Edge_R , layer=self.layer_deep_grid).put()

        
            # add the text
            text_height = 100
            nd.Font('cousine').text(text=self.text_bottom, height=text_height, align='cb', layer=self.text_layer).put(0, -self.full_size_y + self.text_offset_y)
            nd.Font('cousine').text(text=self.text_top, height=text_height, align='ct', layer=self.text_layer).put(0, self.full_size_y - self.text_offset_y)


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








class MZM:
    '''
    Mach Zehnder Modulator
    '''
    cell_MZM = "MZM"
    cell_WG = "WG"

    def __init__(self, width_Metal, length_Metal, width_WG, length_WG, width_MMI, length_MMI, length_WG_MMI, space, gap_MMI_WG, gap, layer_Struct=Layer.Struct, layer_Metal = Layer.MET1, layer_text_Metal = Layer.TXT_MET1, layer_text_WG = Layer.TXT_Struct, text_MZM = "", text_WG = "", text_MMI = ""):
        '''
        

        Parameters
        ----------
        width_Metal : int/float
            Width of the metal electrodes.
        length_Metal : int/float
            Length of the metal electrodes.
        width_WG : int/flaot
            Width of the Waveguide.
        length_WG : int/float
            Length of the Waveguide.
        width_MMI : int/float
            Width of the Input/Output MMIs.
        length_MMI : int/float
            Length MMIs.
        length_WG_MMI : int/float
            Length of the Waveguides of the MMIs.
        space : int/float
            Space between the Input and Output waveguides
        gap_MMI_WG : int/float
            Gap between the MMI Waveguides.
        gap : int/float
            Gap between the metal electrodes and the Waveguides.
        layer_Struct : list, optional
            Layers Definition, do not change! The default is Layer.DEEP_GRID.
        layer_Metal : list, optional
            Layers Definition, do not change! The default is Layer.MET1.
        layer_text_Metal : list, optional
            Layers Definition, do not change! The default is Layer.TXT_MET1.
        layer_text_WG :list, optional
            Layers Definition, do not change! The default is Layer.TXT_Struct.
        text_MZM : str, optional
            Label on the MZM. The default is "".
        text_WG : str, optional
            Label the MZM Waveguides. The default is "".
        text_MMI : str, optional
            Label the MMIs. The default is "".

        Returns
        -------
        None.

        '''
        self.width_Metal = width_Metal
        self.length_Metal = length_Metal
        self.width_WG = width_WG
        self.length_WG = length_WG
        self.width_MMI = width_MMI
        self.length_MMI = length_MMI
        self.gap = gap
        self.gap_MMI_WG = gap_MMI_WG
        self.space = space
        self.layer_Struct = layer_Struct
        self.layer_Metal = layer_Metal
        self.text_MZM = text_MZM
        self.text_WG = text_WG
        self.layer_text_Metal = layer_text_Metal
        self.layer_text_WG = layer_text_WG
        self.length_WG_MMI = length_WG_MMI
        self.text_MMI = text_MMI


        # create cell
        self._cell = self.create_gds()

    def create_gds(self):
        '''
        

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.

        '''
        with nd.Cell(MZM.cell_MZM) as cell:


            # #Create WG
            cell_WG_Top = [(0, self.width_WG / 2), (self.length_WG / 2, self.width_WG / 2),(self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, self.width_WG / 2), (0, self.width_WG / 2)]
            # nd.Polygon(points=cell_WG, layer=self.layer_Struct).put(0, 0, 0)
            WG_1 = nd.Polygon(points=cell_WG_Top, layer=self.layer_Struct).put(0, self.width_Metal/2 + self.gap + self.width_WG / 2, 0)


            cell_WG_Bot = [(0, self.width_WG / 2), (self.length_WG / 2, self.width_WG / 2),(self.length_WG / 2, -self.width_WG / 2), (-self.length_WG / 2, -self.width_WG / 2),(-self.length_WG / 2, self.width_WG / 2), (0, self.width_WG / 2)]
            # nd.Polygon(points=cell_WG, layer=self.layer_Struct).put(0, 0, 0)
            WG_2 = nd.Polygon(points=cell_WG_Bot, layer=self.layer_Struct).put(0, -self.width_Metal/2 - self.gap - self.width_WG / 2, 0)




            # cretae Metal and GND Polygons
            cell_Signal = [(0, self.width_Metal / 2), (self.length_Metal / 2, self.width_Metal / 2),(self.length_Metal / 2, -self.width_Metal / 2),(-self.length_Metal / 2, -self.width_Metal / 2),(-self.length_Metal / 2, self.width_Metal / 2), (0, self.width_Metal / 2)]
            # nd.Polygon(points=cell_Signal, layer=self.length_Metal).put(0, self.width_Metal/2 + self.gap/2, 0)
            nd.Polygon(points=cell_Signal, layer=self.length_Metal).put()

            cell_GND_Top = [(0, self.width_Metal / 2), (self.length_Metal / 2, self.width_Metal / 2), (self.length_Metal / 2, -self.width_Metal / 2),(-self.length_Metal / 2, -self.width_Metal / 2), (-self.length_Metal / 2, self.width_Metal / 2), (0, self.width_Metal / 2)]
            # nd.Polygon(points=cell_GND_Top, layer=self.length_Metal).put(0, -self.width_Metal/2 -self.gap/2,0)
            nd.Polygon(points=cell_GND_Top, layer=self.length_Metal).put(0, self.width_Metal + self.gap * 2 + self.width_WG, 0)

            cell_GND_Bot = [(0, self.width_Metal / 2), (self.length_Metal / 2, self.width_Metal / 2), (self.length_Metal / 2, -self.width_Metal / 2), (-self.length_Metal / 2, -self.width_Metal / 2), (-self.length_Metal / 2, self.width_Metal / 2), (0, self.width_Metal / 2)]
            # nd.Polygon(points=cell_GND, layer=self.length_Metal).put(0, -self.width_Metal / 2 - self.gap / 2, 0)
            nd.Polygon(points=cell_GND_Bot, layer=self.length_Metal).put(0, - self.width_Metal - self.gap * 2 - self.width_WG, 0)





            # Create MZMs on Input and Output
            MMI_Pos_x  = self.length_Metal/2 + self.length_MMI/2 + self.length_WG_MMI + self.space



            MMI_In = MMI1x2(self.width_MMI, self.length_MMI, self.width_WG, self.length_WG_MMI, self.gap_MMI_WG, layer_Struct=self.layer_Struct).put(-MMI_Pos_x)
            MMI_Out = MMI1x2(self.width_MMI, self.length_MMI, self.width_WG, self.length_WG_MMI, self.gap_MMI_WG, layer_Struct=self.layer_Struct).put(MMI_Pos_x, 0, 180)


            # create Pins WG
            # nd.Pin('a0', width=self.width_WG).put(-self.length_WG/2, 0, 180)
            # nd.Pin('b0', width=self.width_WG).put(self.length_WG/2, 0, 0)

            nd.Pin('WG_Top_Out', width=self.width_WG).put(-self.length_WG / 2, self.width_Metal / 2 + self.gap + self.width_WG / 2, 180)
            nd.Pin('WG_Top_In', width=self.width_WG).put(self.length_WG / 2, self.width_Metal / 2 + self.gap + self.width_WG / 2, 0)

            nd.Pin('WG_Bot_Out', width=self.width_WG).put(-self.length_WG / 2, -self.width_Metal / 2 - self.gap - self.width_WG / 2, 180)
            nd.Pin('WG_Bot_In', width=self.width_WG).put(self.length_WG / 2, -self.width_Metal / 2 - self.gap - self.width_WG / 2, 0)

            # create Pins Signal and GND
            # nd.Pin('Signal_a0', width=self.width_Metal).put(-self.length_Metal/2, self.width_Metal/2 + self.gap/2, 180)
            # nd.Pin('Signal_b0', width=self.width_Metal).put(self.length_Metal/2, self.width_Metal/2 + self.gap/2, 0)

            nd.Pin('Signal_a0', width=self.width_Metal).put(-self.length_Metal / 2, 0, 180)
            nd.Pin('Signal_b0', width=self.width_Metal).put(self.length_Metal / 2, 0, 0)

            # nd.Pin('GND_a0', width=self.width_Metal).put(-self.length_Metal/2, -self.width_Metal/2 -self.gap/2, 180)
            # nd.Pin('GND_b0', width=self.width_Metal).put(self.length_Metal/2,  -self.width_Metal/2 -self.gap/2, 0)

            nd.Pin('GND_Top_Out', width=self.width_Metal).put(-self.length_Metal / 2, self.width_Metal + self.gap * 2 + self.width_WG, 180)
            nd.Pin('GND_Top_In', width=self.width_Metal).put(self.length_Metal / 2, self.width_Metal + self.gap * 2 + self.width_WG, 0)

            nd.Pin('GND_Bot_Out', width=self.width_Metal).put(-self.length_Metal / 2, - self.width_Metal - self.gap * 2 - self.width_WG, 180)
            nd.Pin('GND_Bot_In', width=self.width_Metal).put(self.length_Metal / 2, - self.width_Metal - self.gap * 2 - self.width_WG, 0)
            nd.put_stub()

            # create S-Bends from Pin Locations

            x1, y1, a1 = MMI_In.pin["MMI_Out_Bot"].xya()
            y2 = self.width_Metal / 2 + self.gap + self.width_WG / 2

            

            MMI_In_Length = -self.length_WG / 2 - x1
            MMI_In_Top_Offset = y2 + y1
            Bends_Pos_x = self.length_Metal/2  + self.space 

            Out_Bot = SBends_Bezier(width_WG = self.width_WG, Bend_Length = MMI_In_Length, Offset = MMI_In_Top_Offset).put(x1, MMI_In_Top_Offset/2 + self.gap_MMI_WG/2 + self.width_WG/2 , 0) # -Bends_Pos_x#self.gap_MMI_WG/2 
            Out_Top = SBends_Bezier(width_WG = self.width_WG, Bend_Length = MMI_In_Length, Offset = MMI_In_Top_Offset, reverse = 1).put(x1, -MMI_In_Top_Offset/2 - self.gap_MMI_WG/2 - self.width_WG/2, 0) # self.gap_MMI_WG/2 + self.width_WG/2
            In_Bot = SBends_Bezier(width_WG = self.width_WG, Bend_Length = MMI_In_Length, Offset = MMI_In_Top_Offset).put(self.length_WG / 2, -MMI_In_Top_Offset/2 - self.gap_MMI_WG/2 - self.width_WG/2, 0)#put(Bends_Pos_x, +self.gap_MMI_WG/2 + self.width_WG/2, 180)
            In_Bot = SBends_Bezier(width_WG = self.width_WG, Bend_Length = MMI_In_Length, Offset = MMI_In_Top_Offset, reverse = 1).put(self.length_WG / 2, MMI_In_Top_Offset/2 + self.gap_MMI_WG/2 + self.width_WG/2 , 0)#put( Bends_Pos_x, -self.gap_MMI_WG/2 - self.width_WG/2, 180)
         
            


            # add the text
            text_height_MZM = self.width_MMI / 2
            text_height_WG = self.width_WG / 2
            text_height_MMI = self.width_MMI / 2
            text_MMI_pos = self.length_Metal/2 + self.length_MMI/2 + self.length_WG_MMI  + self.space
            nd.Font('cousine').text(text=self.text_MZM, height=text_height_MZM, align='cb', layer=self.layer_text_Metal).put(0, -text_height_MZM/2)
            nd.Font('cousine').text(text=self.text_WG, height=text_height_WG, align='ct', layer=self.layer_text_WG).put(0, self.width_Metal/2 + self.gap + self.width_WG / 2 + text_height_WG/2)
            nd.Font('cousine').text(text=self.text_MMI + " In", height=text_height_MMI, align='ct', layer=self.layer_text_WG).put(-text_MMI_pos, self.width_MMI/2 + self.gap + self.width_WG / 2 + text_height_WG/2)
            nd.Font('cousine').text(text=self.text_MMI + " Out", height=text_height_MMI, align='ct', layer=self.layer_text_WG).put(text_MMI_pos , self.width_MMI/2 + self.gap + self.width_WG / 2 + text_height_WG/2)
       
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






# parameters = {'length_Metal': 500, 'width_Metal': 50, 'width_WG':2, 'length_WG':500, 'length_MMI':20, 'width_MMI': 10, 'length_WG_MMI':5, 'space': 100, 'gap_MMI_WG':5, 'gap':5, "text_MZM": "MZM Test Martin", "text_WG": "WG Test Martin", "text_MMI": "MMI"}
# MZM1 = MZM(**parameters).put()



# nd.export_gds()



class DirectionalCoupler:
    '''
    Directional Coupler
    '''
    cell_name = "DirectionalCoupler"
    def __init__(self, length_DC, width_WG, gap, layer_Struct=Layer.Struct, spacing = None, lenght_bend = None, pins = True):
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
            # space = self.spacing/2 + self.gap/2  #+ self.width_WG / 2
            space = self.spacing + self.gap
            gap =  self.gap /2 +self.width_WG/2


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
                nd.put_stub()
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





# parameters = {"length_DC":100, "width_WG":2, "gap":2, "spacing": 40, "lenght_bend": 30}
# DC1 = DirectionalCoupler(**parameters).put(0,0,0)


# parameters = {'length_Metal': 500, 'width_Metal': 50, 'width_WG':2, 'length_WG':500, 'length_MMI':20, 'width_MMI': 10, 'length_WG_MMI':5, 'space': 100, 'gap_MMI_WG':5, 'gap':5, "text_MZM": "MZM Test Martin", "text_WG": "WG Test Martin", "text_MMI": "MMI"}
# MZM1 = MZM(**parameters).put()



# nd.export_gds()