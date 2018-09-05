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
      });
  
      // Use the first sample from the list to build the initial plots
      //const firstSample = sampleNames[0];
      //buildCharts(firstSample);
      //buildMetadata(firstSample);
    });
  }

init();