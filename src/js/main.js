// This file is used for your custom scripts.
document.addEventListener('DOMContentLoaded', function () {
    // Mobile menu toggle
    const mobileMenuButton = document.querySelector('[aria-controls="mobile-menu"]');
    const mobileMenu = document.getElementById('mobile-menu');

    mobileMenuButton.addEventListener('click', function () {
        const expanded = this.getAttribute('aria-expanded') === 'true' || false;
        this.setAttribute('aria-expanded', !expanded);
        mobileMenu.classList.toggle('hidden');
    });

    // Profile dropdown toggle
    const userMenuButton = document.getElementById('user-menu-button');
    const userMenu = userMenuButton.nextElementSibling;

    userMenuButton.addEventListener('click', function () {
        const isExpanded = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', !isExpanded);
        userMenu.classList.toggle('hidden');
    });
});

