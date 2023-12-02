function alertFunction() {
  
    emaillog = document.getElementById('form2Example1').value;
    passwordlog = document.getElementById('form2Example2').value;


    const xmlhttp = new XMLHttpRequest();
      xmlhttp.onload = function() {
        document.getElementById("form2Example1").innerHTML = this.responseText;
      }
      xmlhttp.open("GET", "../../be/index.php");
    xmlhttp.send();
}
