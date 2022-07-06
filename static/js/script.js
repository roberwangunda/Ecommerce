function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }

function Apple_phone() {
  var image = document.createElement('img');
  var div = document.getElementById('Apples');
  image.src = "https://media1.tenor.com/images/29b1fd9b721f82161ae84e10c9cd2c20/tenor.gif?itemid=16499471" 
  div.appendChild(image);
}