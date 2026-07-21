// Nohrskov Fonden — main.js

// Sticky header shadow
const header = document.querySelector('.site-header');
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 10);
});

// Mobile burger
const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav');
burger.addEventListener('click', () => {
  burger.classList.toggle('active');
  nav.classList.toggle('open');
});

// Dropdown toggles (click for touch, hover handled in CSS)
document.querySelectorAll('.nav-item > button.nav-link').forEach(btn => {
  btn.addEventListener('click', e => {
    e.stopPropagation();
    const item = btn.parentElement;
    document.querySelectorAll('.nav-item.open').forEach(o => { if (o !== item) o.classList.remove('open'); });
    item.classList.toggle('open');
  });
});
document.addEventListener('click', () => {
  document.querySelectorAll('.nav-item.open').forEach(o => o.classList.remove('open'));
});

// Reveal on scroll
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
