/**
 * Tailwind CSS Configuration
 * 
 * Why needed: Tailwind CSS is a utility-first CSS framework that allows you to
 * style components quickly using pre-defined classes, eliminating the need to
 * write custom CSS for most styling needs.
 */

import type { Config } from 'tailwindcss'

const config: Config = {
  // Files to scan for Tailwind classes
  // Why needed: Tailwind needs to know which files to analyze to include
  // only the CSS classes you actually use in your final bundle
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',      // Pages directory (if using Pages Router)
    './components/**/*.{js,ts,jsx,tsx,mdx}',  // Components directory
    './app/**/*.{js,ts,jsx,tsx,mdx}',         // App directory (App Router)
  ],
  
  // Theme customization
  // Why needed: Allows you to extend Tailwind's default theme with custom
  // colors, spacing, fonts, and other design tokens
  theme: {
    extend: {
      // Custom background images
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',  // Radial gradient utility
        'gradient-conic': 'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',  // Conic gradient utility
      },
    },
  },
  
  // Tailwind plugins
  // Why needed: Plugins can add new utilities, components, or modify existing behavior
  plugins: [],
}

export default config 