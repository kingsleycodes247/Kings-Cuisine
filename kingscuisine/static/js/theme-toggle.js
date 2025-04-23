document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('theme-toggle');
    const body = document.body;
    const icon = toggleButton.querySelector('i');

    // Check for saved theme preference
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-theme');
        icon.classList.remove('bi-moon-stars-fill');
        icon.classList.add('bi-sun-fill');
    }

    // Toggle theme on button click
    toggleButton.addEventListener('click', () => {
        body.classList.toggle('dark-theme');
        if (body.classList.contains('dark-theme')) {
            icon.classList.remove('bi-moon-stars-fill');
            icon.classList.add('bi-sun-fill');
            localStorage.setItem('theme', 'dark');
        } else {
            icon.classList.remove('bi-sun-fill');
            icon.classList.add('bi-moon-stars-fill');
            localStorage.setItem('theme', 'light');
        }
    });
});
