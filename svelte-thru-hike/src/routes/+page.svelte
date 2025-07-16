<script>

	import maplibregl from 'maplibre-gl';
	import 'maplibre-gl/dist/maplibre-gl.css';
	import { onMount } from 'svelte';


	onMount(async () => {

        const response = await fetch('/trails.geojson');
        let trailData = await response.json();

		let map = new maplibregl.Map({
			container: 'map',
			style: 'https://api.maptiler.com/maps/outdoor-v2/style.json?key=5eBWiA209yLTdiXplZ1u',
			center: [-118, 37],
			zoom: 7
		});

		map.on('load', () =>{
			let nav = new maplibregl.NavigationControl();
			map.addControl(nav, 'top-right');

			map.addSource('trails', {
				type: "geojson",
				data: trailData
			});

			map.addLayer({
				id: 'trails-layer',
				type: 'line',
				source: 'trails',
				paint: {
					'line-color': '#FFFF00',
					'line-width': 3
				}
			}); 
		});
	});
</script>

<main>
	<div id="heading"><h1>Thru-Hike Planner 0.0.1</h1></div>
	<div id="map"></div>
</main>

<style>
	#heading {
		height: 10vh;
	}
	#map {
		border: 2px solid #333;
		height: 85vh;
	}
	main {
		text-align: center;
		padding: 0px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		font-size: 4em;
		font-weight: 100;
		margin: 0;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>