# WGEW - Walnut Gulch Expiremental Watershed  
The Walnut Gulch Experimental Watershed in Tombstone, AZ is one of the most studied experimental watersheds in the US.  There are numerous raingage monitoring stations, numerous runoff flumes, and other earth process monitoring insruments located throughout the watershed.  

## Obtaining the Raingage Instrumentation Data  
1. Access the [SWRC DAP](https://www.tucson.ars.ag.gov/dap/) site.
1. Select the [SWRC Open Data Hub](https://swrc-usdaars.hub.arcgis.com/) link.  
2. Select the [Instrumentation](https://swrc-usdaars.hub.arcgis.com/search?tags=flux%2Cinstrumentation%2Cinstrument%2Craingage%2Cflume%2Ctank%2Cmet%2Ceddy%2520covariance) link.  
3. Select the [SWRC DAP Instrumentation](https://swrc-usdaars.hub.arcgis.com/datasets/2a086d8ac2d64ff0bea7e294c0721447_0/explore) link.    
4. Select the Download button in the Summary pane.  
5. Download the data using one of the provided formats (e.g., csv).  

## Running Jupyter Notebook  
Assuming python 3 or later installed.  
1. Create a project python virtualenv.  
`python -m venv .venv`  
2. Activate the virtualenv  
`source .venv/bin/activate`  
or  
`venv/Scripts/activate.bat`  
or  
`venv/Scripts/activate.ps1`  
3. Install jupyter using pip.  
`pip install jupyter`  
4. Start the jupter notebook server.  
`jupyter-notebook`  
