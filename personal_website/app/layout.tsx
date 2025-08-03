/**
 * Root Layout Component
 * 
 * Why needed: This is the root layout that wraps every page in your Next.js app.
 * It defines the basic HTML structure, includes global styles, sets up fonts,
 * and provides consistent navigation across all pages.
 */

import type { Metadata } from 'next'
import { Inter } from 'next/font/google'  // Google Fonts integration
import './globals.css'  // Global CSS styles
import Navigation from '@/components/Navigation'  // Navigation component

// Load Inter font from Google Fonts with Latin subset
// Why needed: Optimized font loading improves performance and user experience
const inter = Inter({ subsets: ['latin'] })

// Metadata for SEO and social sharing
// Why needed: Helps search engines understand your site and improves social media sharing
export const metadata: Metadata = {
  title: 'Personal Website',  // Page title shown in browser tab
  description: 'Welcome to my personal website',  // Meta description for SEO
}

// Root layout component that wraps all pages
export default function RootLayout({
  children,  // This will be the page content
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Navigation />  {/* Navigation appears on every page */}
        {children}      {/* Page-specific content */}
      </body>
    </html>
  )
} 