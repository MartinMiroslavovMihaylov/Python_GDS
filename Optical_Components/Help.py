# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:12:19 2024

@author: MartinMihaylov
"""

"""
This is the Help Module for your Python GDS SCT Lib with nazca

"""


def Help(Subject = None):
    if Subject is None:
        raise ValueError("Help can be called with Help(str(subject)). Subject can be choosen from 'Boarder', 'Coupler', 'Modulators', 'S_Bends', 'Waveguides' and 'Export GDSII' !! ")
    
    
    elif type(Subject) == dict:
        print('i am in the dict part')
        listSub = ['Boarder', 'Coupler', 'Modulators', 'S_Bends', 'Waveguides', 'Export GDSII']
        listExamp = [1]
        key = list(Subject.keys())
        val = list(Subject.values())
        _help = HelpSubject()
        if key[0] == "Boarder" and val[0] in listExamp:
            _help.Help_Objects(key[0])
            _help.Example(key[0], int(val[0]))
        elif key[0] == "Coupler" and val[0] in listExamp:
            _help.Help_Objects(key[0])
            _help.Example(key[0], int(val[0]))
        elif key[0] == "Modulators" and val[0] in listExamp:
            _help.Help_Objects(key[0])
            _help.Example(key[0], int(val[0]))
        elif key[0] == "S_Bends" and val[0] in listExamp:
            _help.Help_Objects(key[0])
            _help.Example(key[0], int(val[0]))
        elif key[0] == "Waveguides" and val[0] in listExamp:
            _help.Help_Objects(key[0])
            _help.Example(key[0], int(val[0]))
        elif key[0] == "Export GDSII" and val[0] in listExamp:
            _help.Help_Objects(key[0])
            _help.Example(key[0], int(val[0]))
        elif key[0] not in listSub:
            raise ValueError("Help can be called with Help(str(subject)). Subject can be choosen from 'Boarder', 'Coupler', 'Modulators', 'S_Bends', 'Waveguides' and 'Export GDSII' !! ")
            
            
    elif type(Subject) == str :
        print('i am in the String part')
        _help = HelpSubject()
        if Subject == "Boarder":
            _help.Help_Objects(Subject)
        elif Subject == "Coupler":
            _help.Help_Objects(Subject)
        elif Subject == "Modulators":
            _help.Help_Objects(Subject)
        elif Subject == "S_Bends":
            _help.Help_Objects(Subject)
        elif Subject == "Waveguides":
            _help.Help_Objects(Subject)
        elif Subject == "Export GDSII":
            _help.Help_Objects(Subject)
        else:
            raise ValueError("Help can be called with Help(str(subject)). Subject can be choosen from 'Boarder', 'Coupler', 'Modulators', 'S_Bends', 'Waveguides' and 'Export GDSII' !! ")

        

    
class HelpSubject:
    

    @classmethod
    def Help_Objects(self, Subject):
        
        if Subject == 'Boarder':
            print("""
            # ============================================================================= #
            #                Welcome to the Help Menu for Python  GDSII generation with     #
            #                nazca. This Help menu is for the Boarder Function. This        #
            #                function will help you generate your chip boardes or your      #
            #                area. Boarded need some parameters that need to be passed      #
            #                (see below). To call the function use:                         #
            #                                                                               #
            #                parameters = {"chip_size_x": 10000, "chip_size_y": 7000}       #
            #                Border(**parameters).put()                                     #     
            #                                                                               #
            #                For example on hot to use the function use: Help({'Boarder':1})#
            # ============================================================================= #
            
            
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
             text_bottom : str, optional
                 An Text that appears under the chip main Frame. The default is "".
             text_top : str, optional
                 An Text that appears over the chip main Frame. The default is "".
    
            Returns
            -------
            None.
    
    
            """)
            
            
        elif Subject == 'Coupler':
            print("""
            # ============================================================================= #
            #                Welcome to the Help Menu for Python  GDSII generation with     #
            #                nazca. This Help menu is for the Coupler Function. This        #
            #                function will help you generate optical coupler components     #
            #                such as  2x1 MMI, Directional coupler or Y Junctions. To       #
            #                use this functios you will need parameters to pass (see below).#
            #                To call the functions use:                                     #
            #                                                                               #
            #                # Basic 2x1 MMI                                                #
            #               parameters = {"width_MMI":15, "length_MMI":100, "width_WG":2, "length_WG":50, "gap":3}
            #               MMi1 = MMI1x2(**parameters).put(0,300,0)                        #   
            #                                                                               #
            #               # 2x1 MMI with S_Bends                                          #
            #               parameters = {"width_MMI":15, "length_MMI":50, "width_WG":2, "length_WG":10, "gap":1, "spacing": 20, "lenght_bend": 40}
            #               MMi1 = MMI1x2(**parameters).put(0,200,0)                        #  
            #                                                                               #
            #               # Directional coupler                                           #
            #               parameters = {"length_DC":100, "width_WG":2, "gap":2, "spacing": 40, "lenght_bend": 40}
            #               DC1 = DirectionalCoupler(**parameters).put(0, -200, 0)          # 
            #                                                                               #
            #               # Y Junctions                                                   #
            #               parameters = {"length":20, "width_WG":2, "gap":10, "spacing":40, "Bend_Length":30}
            #               YJunction(**parameters).put(0,-300,0)                           #
            #                                                                               #
            #                For example on hot to use the function use: Help({'Coupler':1})#
            # ============================================================================= #
            
            
            Parameters 2x1 MMI  
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
            
            
            
            
            
            
            Parameters Directional Coupler
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
            
            
            
            
            
            
            Parameters Y-Junction
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
    
    
            """)
            
            
        elif Subject == 'Modulators':
            print("""
            # ============================================================================= #
            #                Welcome to the Help Menu for Python  GDSII generation with     #
            #                nazca. This Help menu is for the Modulators Function. This     #
            #                function will help you generate an MZM (for now)               #
            #                Modulators need some parameters that need to be passed         #
            #                (see below). To call the function use:                         #
            #                                                                               #
            #                # MZM                                                          #
            #                parameters = {'length_Metal': 500, 'width_Metal': 50, 'width_WG':2, 'length_WG':600, 'length_MMI':20, 'width_MMI': 10, 'length_WG_MMI':10, 'space': 100, 'gap_MMI_WG':5, 'gap':5, "text_MZM": "MZM Test Martin", "text_WG": "WG Test Martin", "text_MMI": "MMI"}
            #                MZM1 = MZM(**parameters).put(0,0,0)                            #
            #                                                                               #
            #             For example on hot to use the function use: Help({'Modulators':1})#
            # ============================================================================= #
            
            
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
    
    
            """)
            
        elif Subject == 'S_Bends':
            print("""
            # ============================================================================= #
            #                Welcome to the Help Menu for Python  GDSII generation with     #
            #                nazca. This Help menu is for the S_Bends Function. This        #
            #                function will help you generate your S_Bends where they are    #
            #                some variations in the Bends mathematical expression. For now  #
            #                an Cubic Bezier, cosinus and Euler Curve are possible. S_Bends #
            #                need some parameters that need to be passed (see below).       #
            #                 To call the function use:                                     #
            #                                                                               #
            #                # S-Bends Cubic Bezier                                         #
            #                parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2}    #
            #                SBend1 = SBends_Bezier(**parameters).put(0,600, 0 )            #
            #                                                                               #
            #                # S-Bend Cosinus Function                                      #
            #                parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2}    #
            #                SBend2 = SBends_Cos(**parameters).put(0,500, 0)                #
            #                                                                               #
            #                # S-Bend Euler Function                                        #
            #                parameters = {"width_WG": 2, "Offset": 10, "Bend_Length": 300} # 
            #                SBend3 = SBend_Euler(**parameters).put(0,400, 0)               #
            #                For example on hot to use the function use: Help({'S_Bends':1})#
            # ============================================================================= #
                
            
            
            Parameters S-Bends Cubic Bezier
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
            
            
            
            
            
            
            Parameters S-Bend Cosinus Function
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
            
            
            
            
            
            
            Parameters Euler curve
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
    
            """)
      
        elif Subject == 'Waveguides':
            print("""
            # ============================================================================= #
            #                Welcome to the Help Menu for Python  GDSII generation with     #
            #                nazca. This Help menu is for the Waveguides . This             #
            #                function will help you generate your straight Waveguides your  #
            #                for you connections between components or test structures.     #
            #                For the moment they are ony straight waveguides and Pin to Pin #
            #                straight waveguides available. This function need some         #
            #                parameters that need to be passed  (see below). To call        #
            #                the function use:                                              #
            #                                                                               #
            #                # Straight Waveguide                                           #
            #                parameters = {"width_WG":1, "length_WG":300}                   #
            #                StrWG1 = StrWG(**parameters).put(0,400,0)                      #     
            #                                                                               #
            #                # Connect two S-Bends with straight Waveguide                  #
            #                parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2}    #
            #                SBend3 = SBends_Bezier(**parameters).put(0,-500, 0)            #
            #                parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2, "reverse":1}
            #                SBend4 = SBends_Bezier(**parameters).put(500,-500, 0)          #
            #                parameters = {"pin2": SBend3.pin["SBendBez_Out"], "pin1": SBend4.pin["SBendBezR_In"]}
            #                StrWG_P2P(**parameters).put()                                  #
            #                                                                               #
            #             For example on hot to use the function use: Help({'Waveguides':1})#
            # ============================================================================= #
            
            
            Parameters Straight Waveguide
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
            
            
            
            
            
            
            Parameters  Straight Waveguide define from Pin to Pin
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
    
            """)
            
            
        elif Subject == 'Export GDSII':
            print("""
            # ============================================================================= #
            #                Welcome to the Help Menu for Python  GDSII generation with     #
            #                nazca. This Help menu is for the Export GDSII Function. This   #
            #                function will help you generate your chip GDSII file.          #
            #                This function need some parameters that need to be passed      #
            #                (see below). To call the function use:                         #
            #                                                                               #
            #                # create GDS in folder                                         #
            #                nd.export_gds(filename = "TestChip_Single.gds")                #     
            #                                                                               #
            #       For example on hot to use the function use: Help({'Export GDSII':1})#
            # ============================================================================= #
            
            
            Parameters
             ----------
             filename : str
                 Name of the GDSII file. the File will be saved in the directory of the script!
             
    
            Returns
            -------
            None.
    
            """)
        else:
            raise ValueError("Invalide object!! The objects can be one of 'Boarder', 'Coupler', 'Modulators', 'S_Bends', 'Waveguides' and 'Export GDSII'!!!")
            
            
    def Example(self, Subject, Number):
        if Number == 1 and Subject == 'Boarder':
            print("""
                    Chip Boarder Example                                   
-----------------------------------------------------------------------------------------------------------
                    from Optical_Components.Boarder import *
                    # Create an Chip 
                    parameters = {"chip_size_x": 10000, "chip_size_y": 7000}
                    Border(**parameters).put()
-----------------------------------------------------------------------------------------------------------
                """)
                
        elif Number == 1 and Subject == 'Coupler':
            print("""
                    Coupler Example                                   
-----------------------------------------------------------------------------------------------------------
                    from Optical_Components.Coupler import *
                    
                    # Basic 2x1 MMI
                    parameters = {"width_MMI":15, "length_MMI":100, "width_WG":2, "length_WG":50, "gap":3}
                    MMi1 = MMI1x2(**parameters).put(0,300,0)
                    
                    # 2x1 MMI with S_Bends 
                    parameters = {"width_MMI":15, "length_MMI":50, "width_WG":2, "length_WG":10, "gap":1, "spacing": 20, "lenght_bend": 40}
                    MMi1 = MMI1x2(**parameters).put(0,200,0)
                    
                    # Directional coupler
                    parameters = {"length_DC":100, "width_WG":2, "gap":2, "spacing": 40, "lenght_bend": 40}
                    DC1 = DirectionalCoupler(**parameters).put(0, -200, 0)
                    
                    # Y Junctions
                    parameters = {"length":20, "width_WG":2, "gap":10, "spacing":40, "Bend_Length":30}
                    YJunction(**parameters).put(0,-300,0)
-----------------------------------------------------------------------------------------------------------
                """)
                
        elif Number == 1 and Subject == 'Modulators':
            print("""
                    Modulators (MZM) Example                                   
-----------------------------------------------------------------------------------------------------------
                    from Optical_Components.Modulators import *
                    
                    # MZM
                    parameters = {'length_Metal': 500, 'width_Metal': 50, 'width_WG':2, 'length_WG':600, 'length_MMI':20, 'width_MMI': 10, 'length_WG_MMI':10, 'space': 100, 'gap_MMI_WG':5, 'gap':5, "text_MZM": "MZM Test Martin", "text_WG": "WG Test Martin", "text_MMI": "MMI"}
                    MZM1 = MZM(**parameters).put(0,0,0)
-----------------------------------------------------------------------------------------------------------
                """)
            
            
        elif Number == 1 and Subject == 'S_Bends':
            print("""
                    S_Bends Example                                   
-----------------------------------------------------------------------------------------------------------
                    from Optical_Components.S_Bends import *
                    
                    # S-Bends Cubic Bezier  
                    parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2}
                    SBend1 = SBends_Bezier(**parameters).put(0,600, 0 )
                    
                    # S-Bend Cosinus Function
                    parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2}
                    SBend2 = SBends_Cos(**parameters).put(0,500, 0)
                    
                    # S-Bend Euler Function
                    parameters = {"width_WG": 2, "Offset": 10, "Bend_Length": 300}  
                    SBend3 = SBend_Euler(**parameters).put(0,400, 0)
                    
                    # S-Bend Euler Function Reverse
                    parameters = {"width_WG": 2, "Offset": 10, "Bend_Length": 300, "reverse":1}  
                    SBend4 = SBend_Euler(**parameters).put(0,400, 0)
-----------------------------------------------------------------------------------------------------------
                """)
                
        elif Number == 1 and Subject == 'Waveguides':
            print("""
                    Waveguides Example                                   
-----------------------------------------------------------------------------------------------------------
                    from Optical_Components.Waveguides import *
                    
                    # Straight Waveguide
                    parameters = {"width_WG":1, "length_WG":300}
                    StrWG1 = StrWG(**parameters).put(0,400,0)
                    
                    # Connect two S-Bends with straight Waveguide Pin to Pin Waveguide
                    parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2}
                    SBend3 = SBends_Bezier(**parameters).put(0,-500, 0)
                    parameters = {'Bend_Length':300, 'Offset':50, 'width_WG':2, "reverse":1}
                    SBend4 = SBends_Bezier(**parameters).put(500,-500, 0)
                    parameters = {"pin2": SBend3.pin["SBendBez_Out"], "pin1": SBend4.pin["SBendBezR_In"]}
                    StrWG_P2P(**parameters).put()
-----------------------------------------------------------------------------------------------------------
                """)
                
        elif Number == 1 and Subject == 'Export GDSII':
            print("""
                    Export GDSII Example                                   
-----------------------------------------------------------------------------------------------------------
                    # create GDS in folder 
                    nd.export_gds(filename = "TestChip_Single.gds")
-----------------------------------------------------------------------------------------------------------
                """)
                
                
        else:
            raise ValueError("Invalid Key or Value!! The Key can be one of 'Boarder', 'Coupler', 'Modulators', 'S_Bends', 'Waveguides' and 'Export GDSII'! The dictionary value can be only an int(1)!!!")
        
        
