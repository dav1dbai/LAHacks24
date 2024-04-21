// tailwind.config.js
module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    colors: {
      'tab_brown': '#F8D6AE',
      'tab_border_brown': '#BF8148',
      'text_brown' : '#6D4520',
      'deadline_green' : '#45917E'
    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}