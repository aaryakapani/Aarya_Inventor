/**
 * Navigation Component
 * 
 * Why needed: This component provides consistent navigation across all pages.
 * It shows the current page, allows easy navigation between sections,
 * and provides a professional header for your website.
 */

'use client'  // Enables client-side features like usePathname

import Link from 'next/link'  // Next.js optimized link component
import { usePathname } from 'next/navigation'  // Hook to get current page path

export default function Navigation() {
  // Get the current page path for highlighting active navigation
  const pathname = usePathname()

  // Navigation items configuration
  // Why needed: Centralized configuration makes it easy to add/remove pages
  const navItems = [
    { href: '/', label: 'Home' },
    { href: '/about', label: 'About' },
    { href: '/contact', label: 'Contact' },
  ]

  return (
    // Navigation bar with responsive design and dark mode support
    <nav className="bg-white dark:bg-gray-900 shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          
          {/* Logo/Brand section */}
          <div className="flex items-center">
            <Link href="/" className="text-xl font-bold text-gray-900 dark:text-white">
              Aarya's Sandbox
            </Link>
          </div>
          
          {/* Navigation links */}
          <div className="flex items-center space-x-8">
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                  // Highlight active page with different styling
                  pathname === item.href
                    ? 'text-blue-600 dark:text-blue-400'  // Active state
                    : 'text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white'  // Default state
                }`}
              >
                {item.label}
              </Link>
            ))}
          </div>
        </div>
      </div>
    </nav>
  )
} 