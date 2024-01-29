import numpy as np
import nazca as nd
from scipy.special import fresnel
from scipy.optimize import minimize
from Optical_Components.LayerDeff import *



class SBends_Bezier:
    '''
    S-Bends Bezier
    '''
    cell_name = "SBends_Bezier"

    def __init__(self, width_WG, Bend_Length, Offset, layer_Struct=Layer.Struct, layer_text_Pots = Layer.TXT_Ports, layer_Arrow = Layer.ARROW_CLR, reverse = None, pins = True ):
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
        layer_text_Pots : list, optional
            Layers Definition, do not change! The default is Layer.TXT_Ports.
        layer_Arrow : list, optional
            Layers Definition, do not change!The default is Layer.ARROW_CLR.
        reverse : int/float, optional
            Set revers to an  random numbe, for example reverse = 1 to mirror the
            curve on the Y-Axis. The default is None.
        pins : boolen, optional
            Show pins in the GDSII file. The default is True.

        Returns
        -------
        None.

        '''
        self.width_WG = width_WG
        self.Bend_Length = Bend_Length
        self.Offset = Offset
        self.layer_Struct=layer_Struct
        self.layer_text_Pots = layer_text_Pots
        self.layer_Arrow = layer_Arrow
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
                    nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)
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
    








class SBends_Cos:
    '''
    S-Bend Cosinus Function
    '''
    cell_name = "SBends_Cos"

    def __init__(self, width_WG, Bend_Length, Offset, layer_Struct=Layer.Struct, layer_text_Pots = Layer.TXT_Ports, layer_Arrow = Layer.ARROW_CLR, reverse = None):
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
        layer_text_Pots : list, optional
            Layers Definition, do not change! The default is Layer.TXT_Ports.
        layer_Arrow : list, optional
            Layers Definition, do not change! The default is Layer.ARROW_CLR.
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
        self.layer_text_Pots = layer_text_Pots
        self.layer_Arrow = layer_Arrow
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
                nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)
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









def xyal_euler2(radius, angle, number=None):
    x1, y1, a1, l1 = xyal_bend_euler(radius, angle, number)
    x2, y2, a2, l2 = rotate_matrix(x1, y1, a1, l1, -2 * a1[-1], y_flip=True)
    x2, y2, a2, l2 = move_matrix(x2, y2, a2, l2, x1[-1] - x2[-1], y1[-1] - y2[-1], is_inverted=True, l_start=l1[-1])
    return np.concatenate((x1, x2)), np.concatenate((y1, y2)), np.concatenate((a1, a2)), np.concatenate((l1, l2))


def xya_sbend_euler(radius, angle, number=None):
    x1, y1, a1, l1 = xyal_bend_euler(radius, angle, number)
    x2, y2, a2, l2 = rotate_matrix(x1, y1, a1, l1, -2 * a1[-1], y_flip=True)
    x2, y2, a2, l2 = move_matrix(x2, y2, a2, l2, x1[-1] - x2[-1], y1[-1] - y2[-1], is_inverted=True, l_start=l1[-1])
    x3, y3, a3, l3 = rotate_matrix(x1, y1, a1, l1, 0, x_flip=True)
    x3, y3, a3, l3 = rotate_matrix(x3, y3, a3, l3, 2 * a1[-1])
    x3, y3, a3, l3 = move_matrix(x3, y3, a3, l3, x2[-1], y2[-1], l_start=l2[-1])
    x4, y4, a4, l4 = rotate_matrix(x1, y1, a1, l1, 0, x_flip=True, y_flip=True)
    x4, y4, a4, l4 = move_matrix(x4, y4, a4, l4, x3[-1] - x4[-1], y3[-1] - y4[-1], is_inverted=True, l_start=l3[-1])
    return np.concatenate((x1, x2, x3, x4)), np.concatenate((y1, y2, y3, y4)), np.concatenate((a1, a2, a3, a4)), np.concatenate((l1, l2, l3, l4))


def end_radius_from_angle(angle, radius):
    angle_rad = np.radians(angle)
    angle_rad_end = np.pi/2
    return np.sqrt(angle_rad/angle_rad_end)*radius


def radius_from_angle(angle, end_radius):
    angle_rad = np.radians(np.abs(angle))
    angle_rad_end = np.pi/2
    return np.sqrt(angle_rad_end/angle_rad)*end_radius


def radius_from_spacing(offset):
    angle = np.pi/2
    y = fresnel(np.sqrt(2 / np.pi) * np.sqrt(angle))[0]/np.sqrt(2/np.pi)
    return offset/(2*np.sqrt(angle)*y)


def xyl_euler(radius, angle):
    angle_rad = np.radians(angle)
    length_total_2_pi = np.pi/2*2*radius
    coefficient = np.sqrt(2*length_total_2_pi*radius)
    length_total = np.sqrt(angle_rad)*coefficient
    y, x = fresnel(np.sqrt(2/np.pi)*length_total / coefficient)
    return x*coefficient/np.sqrt(2/np.pi), y*coefficient/np.sqrt(2/np.pi), length_total


def xyal_bend_euler(radius, angle, number=None):
    angle_rad = np.abs(np.radians(angle))
    length_total_2_pi = np.pi/2*2*radius
    coefficient = np.sqrt(2*length_total_2_pi*radius)
    length_total = np.sqrt(angle_rad)*coefficient
    number = number if number else max(int(angle_rad*120/(np.pi/2)), 10)
    lengths = np.linspace(0, length_total, number)
    angles = np.rad2deg(np.power(lengths/coefficient, 2))
    y, x = fresnel(np.sqrt(2/np.pi)*lengths / coefficient)
    return x*coefficient/np.sqrt(2/np.pi), y*coefficient/np.sqrt(2/np.pi), angles, lengths


def move_matrix(x, y, a, l, x_center, y_center, is_inverted=False, l_start=0):
    xr = (x+x_center)[::-1] if is_inverted else x+x_center
    yr = (y+y_center)[::-1] if is_inverted else y+y_center
    ar = a[::-1]-180 if is_inverted else a
    lr = l+l_start
    return xr, yr, ar, lr


def rotate_matrix(x, y, a, l, angle, x_flip=False, y_flip=False):
    # Convert degrees to radians
    angle_rad = np.radians(angle)

    # Rotation matrix multiplication to get rotated x & y
    xr = (x * np.cos(angle_rad)) - (y * np.sin(angle_rad))
    yr = (x * np.sin(angle_rad)) + (y * np.cos(angle_rad))
    ar = a + angle
    lr = l

    xr = -xr if y_flip else xr
    yr = -yr if x_flip else yr

    ar = 90 - (ar - 90) if y_flip else ar
    ar = -ar if x_flip else ar

    return xr, yr, ar, lr




class Euler2:
    '''
    Euler curve (Function is tooken from CSEM)
    '''
    cell_name = "Euler2"

    def __init__(self, waveguide_width, angle=90, radius=50, layer_Struct=Layer.Struct, layer_text_Pots = Layer.TXT_Ports, layer_Arrow = Layer.ARROW_CLR):
        '''
        

        Parameters
        ----------
        waveguide_width : int/float
            Waveguide Width
        angle : int/float, optional
            Euler Curve angle. The default is 90.
        radius : int/float, optional
            Curve radius. The default is 50.
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
        self.waveguide_width = waveguide_width
        self.layer_Struct = layer_Struct
        self.layer_text_Pots = layer_text_Pots
        self.layer_Arrow = layer_Arrow
        self.angle = angle
        self.radius = radius
        

        self._cell = self.create_gds()

    def create_gds(self):
        '''
        

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.


        '''
        with nd.Cell(name=Euler2.cell_name) as cell:
            euler = nd.euler(radius=self.radius, angle=self.angle/2, width1=self.waveguide_width, width2=self.waveguide_width, layer = self.layer_Struct)
            euler1_put = euler.put()
            euler2_put = euler.put("b0", flip=True)

            nd.Pin("Euler_In", pin=euler1_put.pin["a0"]).put()
            # nd.Pin("c0", pin=euler1_put.pin["b0"]).put()
            nd.Pin("Euler_Out", pin=euler2_put.pin["a0"]).put()
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







class SBend_Euler:
    '''
    Euler S-Bends tooken from (CSEM)
    '''
    cell_name = "SBendEuler"
    cell_name_bend = "SBendEuler_bend"


    def __init__(self, width_WG, Offset, Bend_Length=None, radius=50, reverse=None, layer_Struct=Layer.Struct, layer_text_Pots = Layer.TXT_Ports, layer_Arrow = Layer.ARROW_CLR):
        '''
        

        Parameters
        ----------
        width_WG : int/float
            Width of the Waveguuide
        Offset : int/float
            Offset between the Input and Output Waveguides.
        Bend_Length : int/float, optional
            Length of the S-Bend. The default is None.
        radius : int/float, optional
            Radius of the S-Bend. The default is 50.
        reverse : int/float, optional
            Set revers to an  random numbe, for example reverse = 1 to mirror the
            curve on the Y-Axis. The default is None.
        layer_Struct : list, optional
            Layers Definition, do not change!. The default is Layer.Struct.
        layer_text_Pots : list, optional
            Layers Definition, do not change! The default is Layer.TXT_Ports.
        layer_Arrow : list, optional
            Layers Definition, do not change! The default is Layer.ARROW_CLR.

        Returns
        -------
        None.

        '''
        self.width_WG = width_WG
        self.layer_Struct = layer_Struct
        self.layer_text_Pots = layer_text_Pots
        self.layer_Arrow = layer_Arrow
        self.Offset = np.abs(Offset)
        self.offset_sign = Offset > 0
        self.Bend_Length = Bend_Length
        self.radius = radius
        self.pin = {}
        self.reverse = reverse

        # take out value
        self.angle = None
        self.length_geo = None

        # create the gds
        self._cell = self.create_gds()

    def create_bend(self, radius, angle):
        '''
        

        Parameters
        ----------
        radius : int/float
            Rdius of the Euler curve.
        angle : int/float
            Angle of the euler bend.

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.

        '''
        if self.reverse:
            with nd.Cell(name=SBend_Euler.cell_name_bend ) as cell:
                x, y, a, l = xya_sbend_euler(radius, angle)
                a_rad = np.radians(a)
                points = [(x[index] + np.sin(a_rad[index])*self.width_WG/2, y[index] - np.cos(a_rad[index])*self.width_WG/2) for index in
                        range(len(x))] + \
                        [(x[index] - np.sin(a_rad[index])*self.width_WG/2, y[index] + np.cos(a_rad[index])*self.width_WG/2) for index in
                        range(len(x))][::-1]

                nd.Polygon(points=points, layer=self.layer_Struct).put(0, -self.Offset/2 ,0)
                nd.Pin("a0", width=self.width_WG).put(x[0], y[0], a[0]-180)
                nd.Pin("b0", width=self.width_WG).put(x[-1], y[-1], a[-1])
                # nd.put_stub()
            return cell

        else:
            with nd.Cell(name=SBend_Euler.cell_name_bend ) as cell:
                x, y, a, l = xya_sbend_euler(radius, angle)
                a_rad = np.radians(a)
                points = [(x[index] + np.sin(a_rad[index])*self.width_WG/2, y[index] - np.cos(a_rad[index])*self.width_WG/2) for index in
                        range(len(x))] + \
                        [(x[index] - np.sin(a_rad[index])*self.width_WG/2, y[index] + np.cos(a_rad[index])*self.width_WG/2) for index in
                        range(len(x))][::-1]

                nd.Polygon(points=points, layer=self.layer_Struct).put(0, -self.Offset/2 ,0)
                nd.Pin("a0", width=self.width_WG).put(x[0], y[0], a[0]-180)
                nd.Pin("b0", width=self.width_WG).put(x[-1], y[-1], a[-1])
                # nd.put_stub()
            return cell


    def create_gds(self):
        '''
        

        Returns
        -------
        cell : cell nezca object
            Return cell object for the nezca library.

        '''
        with nd.Cell(name=SBend_Euler.cell_name) as cell:

            # calculate the length y
            x, y, l = xyl_euler(self.radius, 90/2)
            length_y = x+y
            length_x = x+y

            if self.Offset and self.Offset > 2*length_y:
                self.angle = 45
                euler1 = Euler2(radius=self.radius, angle=self.angle*2, waveguide_width=self.width_WG, layer=self.layer_Struct).put(flip=False if self.offset_sign else True)
                length1 = self.Offset-2*length_y
                nd.strt(self.Offset-2*length_y, width=self.width_WG, layer=self.layer_Struct).put()
                euler2 = Euler2(radius=self.radius, angle=self.angle*2, waveguide_width=self.width_WG, layer=self.layer_Struct).put(flip=True if self.offset_sign else False)
                if self.Bend_Length and self.Bend_Length > 2*length_x:
                    length2 = self.Bend_Length - 2 * length_x
                    euler2 = nd.strt(self.Bend_Length - 2 * length_x, width=self.width_WG, layer=self.layer_Struct).put()
                else:
                    length2 = 0
                self.length_geo = radius_from_angle(self.angle, self.radius) * np.radians(self.angle)*2*4+length1+length2

            else:
                # find minimum of euler
                def minimize_offset(angle):
                    angle_sign = np.sign(angle)
                    angle = np.abs(angle)
                    x, y, l = xyl_euler(self.radius, angle)
                    xy_angle = np.rad2deg(np.arctan(x/y))
                    offset = angle_sign*(y+np.sqrt(np.power(x, 2)+np.power(y, 2))*np.sin(np.radians(xy_angle-(90-angle*2))))
                    return np.power(offset - self.Offset/2, 2)

                def minimize_length(angle_radius):
                    angle = angle_radius[0]
                    radius = angle_radius[1]
                    angle_sign = np.sign(angle)
                    angle = np.abs(angle)
                    x, y, l = xyl_euler(radius, angle)
                    xy_angle = np.rad2deg(np.arctan(x/y))
                    length = angle_sign*(x+np.sqrt(np.power(x, 2)+np.power(y, 2))*np.cos(np.radians(xy_angle-(90-angle*2))))
                    offset = angle_sign*(y+np.sqrt(np.power(x, 2)+np.power(y, 2))*np.sin(np.radians(xy_angle-(90-angle*2))))
                    return np.power(length - self.Bend_Length/2, 2)+np.power(offset - self.Offset/2, 2)

                # if self.Offset > 1e-5:  
                #     if self.Bend_Length:
                #         self.angle, self.radius = minimize(minimize_length, np.array([20, 50])).x
                #     else:
                #         self.angle = minimize(minimize_offset, np.array([20])).x[0]
                #     euler1 = euler2 = self.create_bend(self.radius, self.angle).put(flip=False if self.offset_sign else True)
                #     self.length_geo = radius_from_angle(self.angle, self.radius)*np.radians(self.angle)*2*4
                # else:
                #     if self.Bend_Length is None:
                #         self.Bend_Length=0
                #     euler1 = nd.strt(length=self.Bend_Length/2, layer=self.layer_Struct, width=self.width_WG).put()
                #     euler2 = nd.strt(length=self.Bend_Length/2, layer=self.layer_Struct, width=self.width_WG).put()
                #     self.length_geo = self.Bend_Length


                if self.reverse:
                    self.angle, self.radius = minimize(minimize_length, np.array([20, 50])).x
                    euler1 = euler2 = self.create_bend(self.radius, self.angle).put(flip=True)
                    self.length_geo = radius_from_angle(self.angle, self.radius)*np.radians(self.angle)*2*4
                    # create pin
                    self.pin["SBendEulerR_In"] = nd.Pin('SBendEulerR_In', pin=euler1.pin['a0']).put(0,self.Offset/2,0)
                    self.pin["SBendEulerR_Out"] = nd.Pin('SBendEulerR_Out', pin=euler2.pin['b0']).put(self.Bend_Length, -self.Offset/2,0)
                    self.Bend_Length = euler2.pin["b0"].xya()[0]
                    nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)


                else:
                    self.angle, self.radius = minimize(minimize_length, np.array([20, 50])).x
                    euler1 = euler2 = self.create_bend(self.radius, self.angle).put(flip=False)
                    self.length_geo = radius_from_angle(self.angle, self.radius)*np.radians(self.angle)*2*4
                

                    # create pin
                    self.pin[""] = nd.Pin('SBendEuler_In', pin=euler1.pin['a0']).put(0,-self.Offset/2,0)
                    self.pin["SBendEuler_Out"] = nd.Pin('SBendEuler_Out', pin=euler2.pin['b0']).put(self.Bend_Length,self.Offset/2,0)
                    self.Bend_Length = euler2.pin["b0"].xya()[0]
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
    

