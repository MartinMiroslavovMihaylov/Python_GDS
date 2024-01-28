import numpy as np
import nazca as nd
from Optical_Components.LayerDeff import *
from Optical_Components.S_Bends import *
from Optical_Components.Coupler import *




class MZM:
    cell_MZM = "MZM"
    cell_WG = "WG"

    def __init__(self, width_Metal, length_Metal, width_WG, length_WG, width_MMI, length_MMI, length_WG_MMI, space, gap_MMI_WG, gap, layer_Struct= Layer.Struct, layer_text_Struct = Layer.TXT_Struct, layer_Metal = Layer.MET1, layer_text_Metal = Layer.TXT_MET1, layer_text_Pots = Layer.TXT_Ports, layer_Arrow = Layer.ARROW_CLR, text_MZM = "", text_WG = "", text_MMI = ""):
        self.width_Metal = width_Metal
        self.length_Metal = length_Metal
        self.width_WG = width_WG
        self.length_WG = length_WG
        self.width_MMI = width_MMI
        self.length_MMI = length_MMI
        self.length_WG_MMI = length_WG_MMI
        self.gap = gap
        self.gap_MMI_WG = gap_MMI_WG
        self.space = space
        self.layer_Struct = layer_Struct
        self.layer_Metal = layer_Metal
        self.text_MZM = text_MZM
        self.text_WG = text_WG
        self.layer_text_Metal = layer_text_Metal

        self.layer_text_Struct = layer_text_Struct
        self.layer_text_Pots = layer_text_Pots
        self.layer_Arrow = layer_Arrow
        self.text_MMI = text_MMI



        # create cell
        self._cell = self.create_gds()

    def create_gds(self):
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
            nd.Polygon(points=cell_Signal, layer = self.layer_Metal).put()

            cell_GND_Top = [(0, self.width_Metal / 2), (self.length_Metal / 2, self.width_Metal / 2), (self.length_Metal / 2, -self.width_Metal / 2),(-self.length_Metal / 2, -self.width_Metal / 2), (-self.length_Metal / 2, self.width_Metal / 2), (0, self.width_Metal / 2)]
            # nd.Polygon(points=cell_GND_Top, layer=self.length_Metal).put(0, -self.width_Metal/2 -self.gap/2,0)
            nd.Polygon(points=cell_GND_Top, layer = self.layer_Metal).put(0, self.width_Metal + self.gap * 2 + self.width_WG, 0)

            cell_GND_Bot = [(0, self.width_Metal / 2), (self.length_Metal / 2, self.width_Metal / 2), (self.length_Metal / 2, -self.width_Metal / 2), (-self.length_Metal / 2, -self.width_Metal / 2), (-self.length_Metal / 2, self.width_Metal / 2), (0, self.width_Metal / 2)]
            # nd.Polygon(points=cell_GND, layer=self.length_Metal).put(0, -self.width_Metal / 2 - self.gap / 2, 0)
            nd.Polygon(points=cell_GND_Bot, layer = self.layer_Metal).put(0, - self.width_Metal - self.gap * 2 - self.width_WG, 0)





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
            nd.put_stub(pinlayer=self.layer_Arrow, annotation_layer = self.layer_text_Pots)

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
            nd.Font('cousine').text(text=self.text_WG, height=text_height_WG, align='ct', layer= self.layer_text_Struct).put(0, self.width_Metal/2 + self.gap + self.width_WG / 2 + text_height_WG/2)
            nd.Font('cousine').text(text=self.text_MMI + " In", height=text_height_MMI, align='ct', layer= self.layer_text_Struct).put(-text_MMI_pos, self.width_MMI/2 + self.gap + self.width_WG / 2 + text_height_WG/2)
            nd.Font('cousine').text(text=self.text_MMI + " Out", height=text_height_MMI, align='ct', layer= self.layer_text_Struct).put(text_MMI_pos , self.width_MMI/2 + self.gap + self.width_WG / 2 + text_height_WG/2)
       
        return cell






    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)