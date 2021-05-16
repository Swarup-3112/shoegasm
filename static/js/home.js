// ------------------------------- active button -----------------------

var links = document.querySelectorAll('.outlet li button');
links.forEach(function (element) {
  element.addEventListener('click', function (e) 
  {
    e.preventDefault();
    links.forEach(function (element) {
      element.classList.remove('active');
    });
    this.classList.add('active');
  });
});

// ---------------------------- change image ------------------------

console.log("hello")
let lifestyle=document.querySelector('#img1');
let running=document.querySelector("#img2");
let jordan=document.querySelector("#img3");
let basketball=document.querySelector("#img4");
let football=document.querySelector("#img5");

lifestyle.addEventListener( 'click' , () => {
    // document.body.style.backgroundImage = "url('../images/lifestyle.png')";
    console.log("hello");
});

running.addEventListener( 'click' , () => {
  document.body.style.backgroundImage = "url('../images/running.jpg')";
});

jordan.addEventListener( 'click' , () => {
  document.body.style.backgroundImage = "url('../images/jordan.jpg')";
});

basketball.addEventListener( 'click' , () => {
  document.body.style.backgroundImage = "url('../images/Basketball.png')";
});

football.addEventListener( 'click' , () => {
  document.body.style.backgroundImage = "url('../images/Football.jpg')";
});

// ---------------------------- change page ------------------------

function new_releases() {
  window.location = "store.html";
}

function home() {
  window.location = "home.html";
}

function men_sports() {
  window.location = "men-sports.html";
}

function shoe_profile() {
  window.location = "shoe_profile.html";
}

function cart() {
  window.location = "cart.html";
}