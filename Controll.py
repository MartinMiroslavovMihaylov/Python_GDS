from Optical_Components.LayerDeff import *
from Optical_Components.Boarder import *
from Optical_Components.Waveguides import *
from Optical_Components.S_Bends import *
from Optical_Components.Coupler import *
from Optical_Components.Modulators import *
from Optical_Components.Help import * 

import numpy as np


# # =============================================================================
# # Help Section
# # =============================================================================

# # Call for Help 
# Help()


# Help('Boarder')
# Help({'Boarder':1})

# Help('Coupler')
# Help({'Coupler':1})

# Help('Modulators')
# Help({'Modulators':1})

# Help('S_Bends')
# Help({'S_Bends':1})
 
# Help('Waveguides')
# Help({'Waveguides':1})

# Help('Export GDSII')
# Help({'Export GDSII':1})


# ========================================================
# Single Components Example
# ========================================================

# # Create an Chip 
# parameters = {"chip_size_x": 10000, "chip_size_y": 7000}
# Border(**parameters).put()


# # S-Bends Cubic Bezier  
# parameters = {'Bend_Length':300, 'Offset':100, 'width_WG':2}
# SBend1 = SBends_Bezier(**parameters).put(0,600, 0 )

# # S-Bend Cosinus Function
# parameters = {'Bend_Length':300, 'Offset':100, 'width_WG':2}
# SBend2 = SBends_Cos(**parameters).put(0,500, 0)



# # S-Bend Euler Function
# parameters = {"width_WG": 2, "Offset": 100, "Bend_Length": 300}  
# SBend3 = SBend_Euler(**parameters).put(0,400, 0)


# # S-Bend Euler Function Reverse
# parameters = {"width_WG": 2, "Offset": 10, "Bend_Length": 300, "reverse":1}  
# SBend4 = SBend_Euler(**parameters).put(0,400, 0)



# # Straight Waveguide
# parameters = {"width_WG":1, "length_WG":300}
# StrWG1 = StrWG(**parameters).put(0,400,0)



# # Basic 2x1 MMI
# parameters = {"width_MMI":15, "length_MMI":100, "width_WG":2, "length_WG":50, "gap":3}
# MMi1 = MMI1x2(**parameters).put(0,300,0)


# # 2x1 MMI with S_Bends 
# parameters = {"width_MMI":15, "length_MMI":50, "width_WG":2, "length_WG":10, "gap":1, "spacing": 20, "lenght_bend": 40}
# MMi1 = MMI1x2(**parameters).put(0,200,0)


# # MZM
# parameters = {'length_Metal': 500, 'width_Metal': 50, 'width_WG':2, 'length_WG':600, 'length_MMI':20, 'width_MMI': 10, 'length_WG_MMI':10, 'space': 100, 'gap_MMI_WG':5, 'gap':5, "text_MZM": "MZM Test Martin", "text_WG": "WG Test Martin", "text_MMI": "MMI"}
# MZM1 = MZM(**parameters).put(0,0,0)

# # Directional coupler
# parameters = {"length_DC":100, "width_WG":2, "gap":2, "spacing": 40, "lenght_bend": 40}
# DC1 = DirectionalCoupler(**parameters).put(0, -200, 0)

# # Connect two S-Bends with straight Waveguide
# parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2}
# SBend3 = SBends_Bezier(**parameters).put(0,-500, 0)
# parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2, "reverse":1}
# SBend4 = SBends_Bezier(**parameters).put(500,-500, 0)
# parameters = {"pin2": SBend3.pin["SBendBez_Out"], "pin1": SBend4.pin["SBendBezR_In"]}
# StrWG_P2P(**parameters).put()

# # Y Junctions
# parameters = {"length":20, "width_WG":2, "gap":10, "spacing":40, "Bend_Length":30}
# YJunction(**parameters).put(0,-300,0)

# parameters = {"length":20, "width_WG":2, "gap":10, "spacing":40, "Bend_Length":30, "reverse":1}
# YJunction(**parameters).put(0,-300,0)



# # create GDS in folder 
# nd.export_gds(filename = "TestChip_Single.gds")





# # ========================================================
# # Multiple components Macro
# # ========================================================

# # ========================================================
# # Params
# # ========================================================
# Chip_Length = 10000
# Chip_Width = 7000
# WG_Width = 0.775
# WG_Length = 10000
# star_y = 7000/2 

# Bend_Length = 60
# Offset = 40
# space_SBends = 100 


# MMI_length = 10
# MMI_width = 3
# MMI_gap_Outputs = 1
# MMI_spacing_Output = Offset - MMI_gap_Outputs 
# MMI_WG_Length = 10


# MZM_length_Metal = 400
# MZM_length_WG = 500
# MZM_width_Metal = 50
# MZM_gap_Metal_WG = 2
# MZM_Space = 100


# DC_Lenght = 300
# DC_BendsLength = 60
# DC_WG_Length = DC_Lenght - DC_BendsLength
# DC_gap = 1
# DC_Space = 40



# YJunction_Length = 50
# YJunction_gap = 10
# YJunction_BendsLength = 40


# # ========================================================
# # Chip Space
# # ========================================================

# parameters = {"chip_size_x": Chip_Length, "chip_size_y": Chip_Width, "text_bottom": "Test Bot", "text_top": "Test Top"}
# Border(**parameters).put()


# # ========================================================
# # Waveguides
# # ========================================================

# vec = np.ones(6) * 40
# new_y = star_y 

# # WG Geom 1
# for i in range(len(vec)):
#     parameters = {"width_WG":WG_Width, "length_WG":WG_Length}
#     StrWG(**parameters).put(-WG_Length/2, new_y - vec[i] - WG_Width, 0)
#     new_y = new_y - vec[i]- WG_Width

# new_y = new_y - 40 - WG_Width

# #WG Geom 2
# for i in range(len(vec)):
#     parameters = {"width_WG":WG_Width, "length_WG":WG_Length}
#     StrWG(**parameters).put(-WG_Length/2, new_y - vec[i] - WG_Width  , 0)
#     new_y = new_y - vec[i]- WG_Width



# # ========================================================
# # S-Bends
# # ========================================================


# new_y = new_y - 80 - WG_Width 
# midPoint = space_SBends/2 + Bend_Length
# Length_WG_In = WG_Length/2 - Bend_Length - space_SBends/2
 


# # BezierCurve
# for i in range(len(vec)):
#     parameters = {'Bend_Length':Bend_Length, 'Offset':Offset, 'width_WG':WG_Width}
#     SBend1 = SBends_Bezier(**parameters).put(-midPoint, new_y - vec[i] - WG_Width, 0)
#     parameters = {'Bend_Length':Bend_Length, 'Offset':Offset, 'width_WG':WG_Width, "reverse":1}
#     SBend2 = SBends_Bezier(**parameters).put(midPoint , new_y - vec[i] - WG_Width, 180)
#     parameters = {"pin1": SBend2.pin["SBendBezR_Out"], "pin2": SBend1.pin["SBendBez_Out"]}
#     StrWG_P2P(**parameters).put()
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_In}
#     InStr = StrWG(**parameters).put(-WG_Length/2, new_y - vec[i] - WG_Width - Offset/2, 0)
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_In}
#     OutStr = StrWG(**parameters).put(midPoint, new_y - vec[i] - WG_Width - Offset/2, 0)
#     new_y = new_y - vec[i]- WG_Width


# new_y = new_y - 80 - WG_Width

# # Cosine Curve

# for i in range(len(vec)):
#     parameters = {'Bend_Length':Bend_Length, 'Offset':Offset, 'width_WG':WG_Width}
#     SBend1 = SBends_Cos(**parameters).put(-midPoint, new_y - vec[i] - WG_Width, 0)
#     parameters = {'Bend_Length':Bend_Length, 'Offset':Offset, 'width_WG':WG_Width, "reverse":1}
#     SBend2 = SBends_Cos(**parameters).put(midPoint , new_y - vec[i] - WG_Width, 180)
#     parameters = {"pin1": SBend2.pin["SBendCosR_Out"], "pin2": SBend1.pin["SBendCos_Out"]}
#     StrWG_P2P(**parameters).put()
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_In}
#     InStr = StrWG(**parameters).put(-WG_Length/2, new_y - vec[i] - WG_Width - Offset/2, 0)
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_In}
#     OutStr = StrWG(**parameters).put(midPoint, new_y - vec[i] - WG_Width - Offset/2, 0)
#     new_y = new_y - vec[i]- WG_Width


# new_y = new_y - 80 - WG_Width


# # Euler Curve

# for i in range(len(vec)):
#     parameters = {'Bend_Length':Bend_Length, 'Offset':Offset, 'width_WG':WG_Width}
#     SBend1 = SBend_Euler(**parameters).put(-midPoint, new_y - vec[i] - WG_Width, 0)
#     parameters = {'Bend_Length':Bend_Length, 'Offset':Offset, 'width_WG':WG_Width,  "reverse":1}
#     SBend2 = SBend_Euler(**parameters).put(midPoint , new_y - vec[i] - WG_Width, 180)
#     parameters = {"pin1": SBend2.pin["SBendEulerR_Out"], "pin2": SBend1.pin["SBendEuler_Out"]}
#     StrWG_P2P(**parameters).put()
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_In}
#     InStr = StrWG(**parameters).put(-WG_Length/2, new_y - vec[i] - WG_Width - Offset/2, 0)
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_In}
#     OutStr = StrWG(**parameters).put(midPoint, new_y - vec[i] - WG_Width - Offset/2, 0)
#     new_y = new_y - vec[i]- WG_Width


# # ========================================================
# # 2x1 MMIs
# # ========================================================


# new_y = new_y - 80 - WG_Width
# vec = np.ones(6) * 80

# for i in range(len(vec)):
#     parameters = {"width_MMI":MMI_width, "length_MMI":MMI_length, "width_WG":WG_Width, "length_WG":MMI_WG_Length, "gap":MMI_gap_Outputs, "spacing": MMI_spacing_Output, "lenght_bend": Bend_Length}
#     MMi1 = MMI1x2(**parameters).put(MMI_length + MMI_WG_Length/2, new_y - vec[i] - WG_Width*2 , 180)
#     PinlocX_Out, PinlocY_Out, PinlocA_Out = MMi1.pin["MMI_Out_Bot"].xya()
#     PinlocX_In, PinlocY_In, PinlocA_In = MMi1.pin["MMI_In"].xya()
#     Length_WG_In = -(WG_Length/2 - PinlocX_In)
#     Length_WG_Out = WG_Length/2 + PinlocX_Out
#     yOff_Output_Top = new_y + MMI_spacing_Output/2 + MMI_gap_Outputs/2 + WG_Width/2
#     yOff_Output_Bot = new_y - MMI_spacing_Output/2 - MMI_gap_Outputs/2 - WG_Width/2
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_In}
#     InStr = StrWG(**parameters).put(WG_Length/2, new_y - vec[i] - WG_Width*2, 0)
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_Out}
#     OutStr_Top = StrWG(**parameters).put(-WG_Length/2, yOff_Output_Top - vec[i] - WG_Width*2, 0)
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_Out}
#     OutStr_Bot = StrWG(**parameters).put(-WG_Length/2, yOff_Output_Bot - vec[i] - WG_Width*2, 0)
#     new_y = new_y - vec[i]- WG_Width*2





# # ========================================================
# # DC 
# # ========================================================

# new_y = new_y - 40 - DC_Space
# vec = np.ones(6) * 80

# for i in range(len(vec)):
#     parameters = {"length_DC":DC_WG_Length, "width_WG":WG_Width, "gap":DC_gap, "spacing": DC_Space, "lenght_bend": DC_BendsLength}
#     DC1 = DirectionalCoupler(**parameters).put(0, new_y- vec[i] - DC_Space*2,0)
#     PinlocX_In_Top , PinlocY_In_Top,a = DC1.pin["DC_In_Top"].xya()
#     PinlocX_In_Bot , PinlocY_In_Bot,a = DC1.pin["DC_In_Bot"].xya()
#     PinlocX_Out_Top , PinlocY_Out_Top,a = DC1.pin["DC_Out_Top"].xya()
#     PinlocX_Out_Bot , PinlocY_Out_Bot,a = DC1.pin["DC_Out_Bot"].xya()
#     Length_WG_In = -(WG_Length/2 - PinlocX_In_Top)
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_In}
#     InStr_Top = StrWG(**parameters).put(WG_Length/2, PinlocY_In_Top, 0)
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_In}
#     InStr_Bot = StrWG(**parameters).put(WG_Length/2, PinlocY_In_Bot, 0)
#     parameters = {"width_WG":WG_Width, "length_WG":-Length_WG_In}
#     OutStr_Top = StrWG(**parameters).put(-WG_Length/2, PinlocY_Out_Top, 0)
#     parameters = {"width_WG":WG_Width, "length_WG":-Length_WG_In}
#     OutStr_Bot = StrWG(**parameters).put(-WG_Length/2, PinlocY_Out_Bot, 0)
#     new_y = new_y - vec[i]- DC_Space*2


# # ========================================================
# # Y Junction
# # ========================================================
    
# new_y = new_y - 80 - DC_Space
# vec = np.ones(6) * 80


# for i in range(len(vec)):
#     parameters = {"length":YJunction_Length, "width_WG":WG_Width, "gap":YJunction_gap, "spacing": DC_Space, "Bend_Length": YJunction_BendsLength, "reverse":1}
#     YJunction1 = YJunction(**parameters).put(0, new_y- vec[i] - WG_Width*2,0)
#     PinlocX_Out, PinlocY_Out, PinlocA_Out = YJunction1.pin["YJunctionR_Out1"].xya()
#     PinlocX_In, PinlocY_In, PinlocA_In = YJunction1.pin["YJunctionR_In"].xya()
#     Length_WG_In = -(WG_Length/2 - PinlocX_In)
#     Length_WG_Out = WG_Length/2 + PinlocX_Out
#     yOff_Output_Top = new_y + MMI_spacing_Output/2 + MMI_gap_Outputs/2 + WG_Width/2
#     yOff_Output_Bot = new_y - MMI_spacing_Output/2 - MMI_gap_Outputs/2 - WG_Width/2
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_In}
#     InStr = StrWG(**parameters).put(WG_Length/2, new_y - vec[i] - WG_Width*2, 0)
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_Out}
#     OutStr_Top = StrWG(**parameters).put(-WG_Length/2, yOff_Output_Top - vec[i] - WG_Width*2, 0)
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_Out}
#     OutStr_Bot = StrWG(**parameters).put(-WG_Length/2, yOff_Output_Bot - vec[i] - WG_Width*2, 0)
#     new_y = new_y - vec[i]- WG_Width*2




# # ========================================================
# # MZM
# # ========================================================
# new_y = new_y - 120 - MZM_width_Metal  
# vec = np.ones(6) * 80
# for i in range(len(vec)):
#     parameters = {'length_Metal': MZM_length_Metal, 'width_Metal': MZM_width_Metal, 'width_WG':WG_Width, 'length_WG':MZM_length_WG, 'length_MMI':MMI_length, 'width_MMI': MMI_width, 'length_WG_MMI':MMI_WG_Length, 'space': MZM_Space, 'gap_MMI_WG':MMI_gap_Outputs, 'gap':MZM_gap_Metal_WG, "text_MZM": "MZM Test Martin", "text_WG": "WG Test Martin", "text_MMI": "MMI"}
#     MZM1 = MZM(**parameters).put(0,new_y - vec[i] - MZM_width_Metal*2 ,0)
#     PinlocX_In = MZM_length_Metal - MZM_Space + MMI_length + MMI_WG_Length*2
#     Length_WG_In = -(WG_Length/2 - PinlocX_In)
#     parameters = {"width_WG":WG_Width, "length_WG":Length_WG_In}
#     InStr = StrWG(**parameters).put(WG_Length/2, new_y - vec[i] - MZM_width_Metal*2 , 0)
#     parameters = {"width_WG":WG_Width, "length_WG": -Length_WG_In}
#     OutStr_Top = StrWG(**parameters).put(-WG_Length/2, new_y - vec[i] - MZM_width_Metal*2, 0)
#     new_y = new_y - vec[i]- MZM_width_Metal*2



# # ========================================================
# # Create GDS
# # ========================================================
# nd.export_gds(filename = "TestChip_Multi.gds")

