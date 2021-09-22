from pysvg import parser
svg=parser.parse('http://www.w3.org/2000/svg')
SW_provinces=['Yun_Nan','Gui_Zhou','Si_Chuan','Guang_Xi','Xi_Zang'] #Five South_West Provinces in China.
for i,province in enumerate(SW_provinces):
    province=svg.getElementByID(province)[0]
    style=province.get_style()
    new_style=style.replace('fill:#808080;','fill:#00%x900;'%(i+7))
    province.set_style(new_style)
svg.save('tmp.svg')