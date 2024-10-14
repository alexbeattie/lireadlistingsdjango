/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
    './listings/templates/**/*.html',
    './listings/static/**/*.js',
    './core/templates/**/*.html',  // Add this if you have templates in core
    ],
    theme: {
        extend: {},
    },
    plugins: [],
}
