document.addEventListener('DOMContentLoaded', function() {
    const passwordField = document.getElementById('password');
    const eyeIcon = document.getElementById('eye-icon');

    eyeIcon.addEventListener('click', function() {
        if (passwordField.type === 'password') {
            passwordField.type = 'text';
            eyeIcon.classList.remove('fa-eye');
            eyeIcon.classList.add('fa-eye-slash');
        } else {
            passwordField.type = 'password';
            eyeIcon.classList.remove('fa-eye-slash');
            eyeIcon.classList.add('fa-eye');
        }
    });
});

// Initialize dropdowns
document.addEventListener('DOMContentLoaded', function () {
    var dropdownEl = document.querySelectorAll('[data-mdb-dropdown-init]');
    dropdownEl.forEach(function (el) {
        new mdb.Dropdown(el);
    });
});



var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('receive_message', function(data) {
    // Handle incoming messages
    console.log(data);
});

function sendMessage() {
    var message = document.getElementById('message').value;
    socket.emit('send_message', {message: message});
}





// Graph
var ctx = document.getElementById("myChart");

var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: [
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
    ],
    datasets: [
      {
        data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
        lineTension: 0,
        backgroundColor: "transparent",
        borderColor: "#007bff",
        borderWidth: 4,
        pointBackgroundColor: "#007bff",
      },
    ],
  },
  options: {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: false,
          },
        },
      ],
    },
    legend: {
      display: false,
    },
  },
});