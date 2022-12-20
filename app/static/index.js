/* initialize variables */
var counter = document.getElementById('counter');

var clonePredecessor100 = document.getElementById('clonePredecessor100');
var clonePredecessor10 = document.getElementById('clonePredecessor10');
var clonePredecessor1 = document.getElementById('clonePredecessor1');

var predecessor100 = document.getElementById('predecessor100');
var predecessor10 = document.getElementById('predecessor10');
var predecessor1 = document.getElementById('predecessor1');

var number100 = document.getElementById('number100');
var number10 = document.getElementById('number10');
var number1 = document.getElementById('number1');

var successor100 = document.getElementById('successor100');
var successor10 = document.getElementById('successor10');
var successor1 = document.getElementById('successor1');

var cloneSuccessor100 = document.getElementById('cloneSuccessor100');
var cloneSuccessor10 = document.getElementById('cloneSuccessor10');
var cloneSuccessor1 = document.getElementById('cloneSuccessor1');


var cloneSuccessor = document.getElementById('cloneSuccessor');
var successor = document.getElementById('successor');
var number = document.getElementById('number');
var predecessor = document.getElementById('predecessor');
var clonePredecessor = document.getElementById('clonePredecessor');

// initiate the number_should (which is the number the counter wheel should always try to rotate to)
// with the number that it currently is so that it doesn't instantly try to change to something
var number_should = parseInt(number100.innerHTML) * 100 +
    parseInt(number10.innerHTML) * 10 +
    parseInt(number1.innerHTML);

predecessor100.innerHTML = Math.floor((number_should - 1) / 100);
predecessor10.innerHTML = Math.floor((number_should - 1) % 100 / 10);
predecessor1.innerHTML = Math.floor((number_should - 1) % 100 % 10);

successor100.innerHTML = Math.floor((number_should + 1) / 100);
successor10.innerHTML = Math.floor((number_should + 1) % 100 / 10);
successor1.innerHTML = Math.floor((number_should + 1) % 100 % 10);

/******** get data for counter *********/

// gets the data from the server and writes it into number_should
function fetchdata() {
    $.ajax({
        url: "/index/refresh-counter",
        type: "get",
    }).done(function (data) {
        number_should = (data["counter"])
    })
}

// sets the counter to a value without animation
function setCounter(toNumber) {
    number100.innerHTML = Math.floor(toNumber / 100);
    number10.innerHTML = Math.floor(toNumber % 100 / 10);
    number1.innerHTML = Math.floor(toNumber % 100 % 10);

    predecessor100.innerHTML = Math.floor((toNumber - 1) / 100);
    predecessor10.innerHTML = Math.floor((toNumber - 1) % 100 / 10);
    predecessor1.innerHTML = Math.floor((toNumber - 1) % 100 % 10);

    successor100.innerHTML = Math.floor((toNumber + 1) / 100);
    successor10.innerHTML = Math.floor((toNumber + 1) % 100 / 10);
    successor1.innerHTML = Math.floor((toNumber + 1) % 100 % 10);
}

setInterval(fetchdata, 4000);

/***** Counter animation ******/

/* functions */

// increases the counter by 1 with the animation
function increaseCounter() {
    var currentNumber = parseInt(number100.innerHTML) * 100 +
        parseInt(number10.innerHTML) * 10 +
        parseInt(number1.innerHTML);

    if (currentNumber >= 999) return;

    // adjust innerHTML
    clonePredecessor100.innerHTML = predecessor100.innerHTML;
    clonePredecessor10.innerHTML = predecessor10.innerHTML;
    clonePredecessor1.innerHTML = predecessor1.innerHTML;

    predecessor100.innerHTML = number100.innerHTML;
    predecessor10.innerHTML = number10.innerHTML;
    predecessor1.innerHTML = number1.innerHTML;

    number100.innerHTML = successor100.innerHTML;
    number10.innerHTML = successor10.innerHTML;
    number1.innerHTML = successor1.innerHTML;

    successor100.innerHTML = Math.floor((currentNumber + 2) / 100);
    successor10.innerHTML = Math.floor((currentNumber + 2) % 100 / 10);
    successor1.innerHTML = Math.floor((currentNumber + 2) % 100 % 10);


    if (currentNumber == 998) {
        successor100.innerHTML = "";
        successor10.innerHTML = "";
        successor1.innerHTML = "";
    }

    // start animation
    successor.classList.add('successorIncrease');
    number.classList.add('numberIncrease');
    predecessor.classList.add('predecessorIncrease');
    clonePredecessor.classList.add('clonePredecessorIncrease');

    // remove itself after being animated
    successor.addEventListener('animationend', function () {
        successor.classList.remove('successorIncrease');
        number.classList.remove('numberIncrease');
        predecessor.classList.remove('predecessorIncrease');
        clonePredecessor.classList.remove('clonePredecessorIncrease');
    })
}

// decreases the counter by 1 with the animation
function decreaseCounter() {
    var currentNumber = parseInt(number100.innerHTML) * 100 +
        parseInt(number10.innerHTML) * 10 +
        parseInt(number1.innerHTML);

    if (currentNumber <= 0) return;

    // adjust innerHTML
    cloneSuccessor100.innerHTML = successor100.innerHTML;
    cloneSuccessor10.innerHTML = successor10.innerHTML;
    cloneSuccessor1.innerHTML = successor1.innerHTML;

    successor100.innerHTML = number100.innerHTML;
    successor10.innerHTML = number10.innerHTML;
    successor1.innerHTML = number1.innerHTML;

    number100.innerHTML = predecessor100.innerHTML;
    number10.innerHTML = predecessor10.innerHTML;
    number1.innerHTML = predecessor1.innerHTML;


    predecessor100.innerHTML = Math.floor((currentNumber - 2) / 100);
    predecessor10.innerHTML = Math.floor((currentNumber - 2) % 100 / 10);
    predecessor1.innerHTML = Math.floor((currentNumber - 2) % 100 % 10);

    if (currentNumber == 1) {
        predecessor100.innerHTML = "";
        predecessor10.innerHTML = "";
        predecessor1.innerHTML = "";
    }


    // start animation
    cloneSuccessor.classList.add('cloneSuccessorDecrease');
    successor.classList.add('successorDecrease');
    number.classList.add('numberDecrease');
    predecessor.classList.add('predecessorDecrease');

    // remove itself after being animated
    successor.addEventListener('animationend', function () {
        cloneSuccessor.classList.remove('cloneSuccessorDecrease');
        successor.classList.remove('successorDecrease');
        number.classList.remove('numberDecrease');
        predecessor.classList.remove('predecessorDecrease');
    })
}

// either increases the counter by 1, decreases it by 1 or does nothing
// depending on if the number it should be is bigger or smaller than the number
// it is right now.
function updateCounter() {
    let current_number = parseInt(number100.innerHTML) * 100 +
        parseInt(number10.innerHTML) * 10 +
        parseInt(number1.innerHTML);

    // number bigger than target number
    if (current_number > number_should) {
        decreaseCounter();
        current_number = parseInt(number100.innerHTML) * 100 +
            parseInt(number10.innerHTML) * 10 +
            parseInt(number1.innerHTML);
    }
    // number smaller than target number
    else if (current_number < number_should) {
        increaseCounter();
        current_number = parseInt(number100.innerHTML) * 100 +
            parseInt(number10.innerHTML) * 10 +
            parseInt(number1.innerHTML);
    }

}



setInterval(updateCounter, 1100);
