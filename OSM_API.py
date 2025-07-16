from pathlib import Path

import geopandas as gpd
import osmnx as ox
import json

G = ox.graph_from_place('Pike National Forest, Colorado, USA', network_type='walk')

gdf_edges = ox.graph_to_gdfs(G, nodes=False)
gdf_edges['geometry'] =  gdf_edges['geometry'].simplify(tolerance=0.0001)

gdf_edges.to_file("trails.geojson", driver="GeoJSON")
