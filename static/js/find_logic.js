// Creating map object
var mymap = L.map('map').setView([37.8, -96], 4);

// adding tile layer
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=' + API_KEY, {
    id: 'mapbox.streets',
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoon: 18
}).addTo(mymap);

console.log("I am working!")

// Link to GeoJSON
var StatesData

d3.json("/states").then(data => {
    StatesData = L.geoJson(data).addTo(map);
    StatesData.addData(geojsonFeature);  
    console.log(data)  
}) 


var geojson;

// Use the pet_stores geojson data
d3.json('/states', function(data) {
    console.log(data);

    // Create a new choropleth layer
    geojson = L.choropleth(data, {

        // Define what property in the features to use
        valueProperty: "BUSINESS",

        // Set color scale
        scale: ["#ffffb2", "#b10026"],

        // Number of breaks in step range
        steps: 100,

        // q for quartile, e for equidistant, k for k-means
        // mode: "q",
        style: {
            // Border color
            color: "#fff",
            weight: 1,
            fillOpacity: 0.8
        },
    
        // Binding a pop-up to each layer
        onEachFeature: function(feature, layer) {
            layer.bindPopup(feature.properties.NAME + ": " + feature.properties.BUSINESS);
        }
    }).addTo(myMap);

});

// Survey variable
document.addEventListener('DOMContentLoaded', bindButtons);

function bindButtons(){
    document.getElementById('submitbreed').addEventListener('click', function(event){
        console.log("####")
        event.preventDefault();
        var apt = document.getElementById("apt").value;
        var train = document.getElementById("train").value;
        var quiet = document.getElementById("quiet").value;
        var highEnergy = document.getElementById("high").value;
        var lowEnergy = document.getElementById("low").value;
        var shed = document.getElementById("shed").value;
        var alone = document.getElementById("alone").value;
        var experienced = document.getElementById("experienced").value;
        var inexperienced = document.getElementById("inexperienced").value;

        var dict = []; // create an empty array
                
        dict.push({
            apt_ans: apt,
            train_ans: train,
            quiet_ans: quiet,
            highEnergy_ans: highEnergy,
            lowEnergy_ans: lowEnergy,
            shed_ans: shed,
            alone_ans: alone,
            exp_ans: experienced,
            inexp_ans: inexperienced
        })
                    
        console.log(dict)
    })
} 


