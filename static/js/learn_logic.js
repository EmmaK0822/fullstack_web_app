function startBar(breed) {
  d3.json(`/breed_traits/${breed}`).then((trait) => {
    
    console.log(trait)

    var data = [
      {
        x: ["Energy Level", "Shedding Level", "Apt Adoptability"],
        y: [trait.energy, trait.shedding, trait.apt_friendly],
        type: 'bar'
      }
    ];

    Plotly.newPlot('buildBar', data);

  });
}


function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/breeds").then((breeds) => {
    breeds.forEach((breed) => {
      selector
        .append("option")
        .text(breed)
        .property("value", breed);
      console.log(breed)
    });

    // Use the first breed from the list to build the initial plots
    const firstSample = breeds[0];
    startBar(firstSample);
  });
}


function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  startBar(newSample);
}
  

init();