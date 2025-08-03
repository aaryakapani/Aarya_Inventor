/**
 * PostCSS Configuration
 * 
 * Why needed: PostCSS is a tool that transforms CSS with JavaScript plugins.
 * It processes your CSS after you write it, adding vendor prefixes and
 * processing Tailwind CSS directives.
 */

module.exports = {
  // PostCSS plugins to run on your CSS
  plugins: {
    tailwindcss: {},    // Processes Tailwind CSS directives (@tailwind, @apply, etc.)
    autoprefixer: {},   // Automatically adds vendor prefixes (-webkit-, -moz-, etc.)
  },
} 