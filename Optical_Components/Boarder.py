import numpy as np
import nazca as nd
from Optical_Components.LayerDeff import *




class Border:
    cell_name = "Border"
    text_offset_x = 150
    text_offset_y = 30


    def __init__(self, chip_size_x, chip_size_y, layer_deep_grid=Layer.DEEP_GRID, text_layer=Layer.TXT_DEEP_GRID, layer_payload=Layer.PAYLOAD, text_bottom = "", text_top = "" ):
        self.chip_size_x = chip_size_x
        self.chip_size_y = chip_size_y
        self.layer_deep_grid = layer_deep_grid
        self.text_bottom = text_bottom
        self.text_top = text_top
        self.text_layer = text_layer
        self.layer_payload = layer_payload
        self.extra_size = 150


        # calculate parameter
        self.border_x = self.chip_size_x / 2 
        self.border_y = self.chip_size_y / 2 
        self.full_size_x = self.extra_size + self.border_x
        self.full_size_y = self.extra_size + self.border_y
        self._cell = self.create_gds()

    def create_gds(self):
        
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
        return self._cell.put(*args, **kwargs)