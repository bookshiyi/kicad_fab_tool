import pcbnew

baseUrl = 'https://www.jlcpcb.com'

# projectName = 
dateTime = time.strftime("%y%m%d", time.localtime())
netlistFileName = 'netlist_'+dateTime+'.ipc'
designatorsFileName = 'designators_'+dateTime+'.csv'
placementFileName = 'pos_'+dateTime+'.csv'
bomFileName = 'bom_'+dateTime+'.csv'
gerberFileName = 'gbr_'+dateTime+'.zip'
gerberArchiveName = 'archive_'+dateTime+'.zip'
outputFolder = 'release'

plotPlan = [
    ("F.Cu", pcbnew.F_Cu, "Top Layer"),
    ("B.Cu", pcbnew.B_Cu, "Bottom Layer"),
    ("In1.Cu", pcbnew.In1_Cu, "Internal plane 1"),
    ("In2.Cu", pcbnew.In2_Cu, "Internal plane 2"),
    ("In3.Cu", pcbnew.In3_Cu, "Internal plane 3"),
    ("In4.Cu", pcbnew.In4_Cu, "Internal plane 4"),
    ("F.SilkS", pcbnew.F_SilkS, "Top Silkscreen"),
    ("B.SilkS", pcbnew.B_SilkS, "Bottom Silkscreen"),
    ("F.Mask", pcbnew.F_Mask, "Top Soldermask"),
    ("B.Mask", pcbnew.B_Mask, "Bottom Soldermask"),
    ("F.Paste", pcbnew.F_Paste, "Top Paste (Stencil)"),
    ("B.Paste", pcbnew.B_Paste, "Bottom Paste (Stencil)"),
    ("Edge.Cuts", pcbnew.Edge_Cuts, "Board Outline")
]
