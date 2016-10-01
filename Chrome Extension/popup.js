document.addEventListener('DOMContentLoaded', function() {
  var link = document.getElementById('submitbutton');
  link.addEventListener('click', function() {
        text = document.getElementById('inputBox').value;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://there-corrector.herokuapp.com/"+text, false);
        xhr.send();
        if (xhr.status == '200'){
          document.getElementById('inputBox').value= xhr.responseText;
          console.log(xhr.statusText);
        }
        else {
          document.getElementById('inputBox').value= 'An error occured. Please try again.';
        }
    });
});
