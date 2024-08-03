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
