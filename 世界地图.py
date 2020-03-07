from pygal_maps_world import maps
from pygal_maps_world.i18n import COUNTRIES
worldmap_chart=maps.World()
worldmap_chart.title='C Countries'
ccodes=[]
for each in COUNTRIES:
    if each.startswith('c')==True:
        ccodes.append(each)
worldmap_chart.add('C Countries',ccodes)
worldmap_chart.render_to_file('map.svg')
