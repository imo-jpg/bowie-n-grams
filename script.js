init();

async function init() {
    let dataset = await d3.csv("songs/lyrics.csv");
    
    dataset.forEach(function(d) {
        d.veracityNum = parseFloat(d.veracityNum);
    })

    let correctMatrix= [];
    let choices = [];
    let choice = 0;
    let currentLyricID = 0;
    let correctChoices = 0;

    for (let i = 0; i < dataset.length; i++) {
        correctMatrix.push(dataset[i].veracityNum);
    }

    let realChoice = d3.select("#real");
    let fakeChoice = d3.select("#fake");
    let submitChoice = d3.select("#submit");
    submitChoice.style("visibility", "hidden");

    let currentLyric = d3.select("#single-lyric");
    currentLyric.text(dataset[currentLyricID].lyric);

    let tracker = d3.select("#num-tracker");
    tracker.text(`${currentLyricID + 1} / 20`);

    let number = d3.select("#number");
    number.text(currentLyricID + 1);

    const compareArrays = (a, b) => {
        for (let i = 0; i < a.length; i++) {
            if (a[i] == b[i]) {
                correctChoices += 1;
            }
        }
    };
      

    realChoice.on("click", function clickReal() {
        realChoice.classed("active-choice", true);
        fakeChoice.classed("active-choice", false);
        submitChoice.style("visibility", "visible");
        choice = 1;
    });

    fakeChoice.on("click", function clickFake() {
        realChoice.classed("active-choice", false);
        fakeChoice.classed("active-choice", true);
        submitChoice.style("visibility", "visible");
        choice = 0;
    });

    submitChoice.on("click", function clickSubmit() {
        choices.push(choice);
        choice = 0;
        submitChoice.style("visibility", "hidden");
        realChoice.classed("active-choice", false);
        fakeChoice.classed("active-choice", false);
        if (currentLyricID < dataset.length - 1) {
            currentLyricID += 1;
            currentLyric.text(dataset[currentLyricID].lyric);
            tracker.text(`${currentLyricID + 1} / 20`);
            number.text(currentLyricID + 1);
        } else {
            currentLyricID = 19;
            submitChoice.remove();
            realChoice.remove();
            fakeChoice.remove();
            tracker.style("visibility", "hidden");
            number.style("visibility", "hidden");
            compareArrays(choices, correctMatrix);
            currentLyric.text("Thank you for playing!");
            currentLyric.append("h3").text("You correctly");
            currentLyric.append("h3").text("assessed");
            currentLyric.append("h3").text(`${correctChoices} lyrics`).style("color", "#ffffff");
            currentLyric.append("h3").text("out of 20");
            d3.select(".menu").append("a").attr("class", "nav").attr("href", "/bowie-n-gram/appendix.html").text("About").style("padding-left", "16px");

        }        
    }); 
}
