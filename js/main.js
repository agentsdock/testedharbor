const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');

if (navToggle && navMenu) {
  navToggle.innerHTML = '<span aria-hidden="true"></span>';
  navToggle.setAttribute('aria-label', 'Open navigation');

  navToggle.addEventListener('click', () => {
    const isOpen = navMenu.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
    navToggle.setAttribute('aria-label', isOpen ? 'Close navigation' : 'Open navigation');
  });

  navMenu.addEventListener('click', (event) => {
    if (event.target.closest('a')) {
      navMenu.classList.remove('is-open');
      navToggle.setAttribute('aria-expanded', 'false');
      navToggle.setAttribute('aria-label', 'Open navigation');
    }
  });
}

const buyButtons = document.querySelectorAll('[data-affiliate]');

buyButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const product = button.getAttribute('data-affiliate');
    console.log(`Affiliate click: ${product}`);
  });
});
