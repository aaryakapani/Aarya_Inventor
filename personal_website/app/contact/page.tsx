/**
 * Contact Page Component
 * 
 * Why needed: This page provides a way for visitors to get in touch with you.
 * It includes a contact form for direct communication and displays alternative
 * contact methods like email and social media links.
 */

'use client'  // Enables client-side interactivity for form handling

import { useState } from 'react'  // React hook for managing form state
import { ExampleSocialLinks } from '@/components/SocialLinks'  // Social links component

export default function Contact() {
  // Form data state management
  // Why needed: Tracks user input in real-time and provides controlled form inputs
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  })

  // Handle form submission
  // Why needed: Processes the form data when user clicks submit
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()  // Prevent default form submission
    // TODO: Implement actual form submission (email service, API call, etc.)
    console.log('Form submitted:', formData)
  }

  // Handle input changes
  // Why needed: Updates form state as user types
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value  // Update specific field while preserving others
    }))
  }

  return (
    // Full-screen container with gradient background
    <div className="min-h-screen bg-gradient-to-br from-green-50 to-emerald-100 dark:from-gray-900 dark:to-gray-800">
      <div className="container mx-auto px-4 py-16">
        <div className="max-w-2xl mx-auto">
          
          {/* Page title */}
          <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-8 text-center">
            Get in Touch
          </h1>
          
          {/* Contact form container */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8">
            
            {/* Contact form */}
            <form onSubmit={handleSubmit} className="space-y-6">
              
              {/* Name input field */}
              <div>
                <label htmlFor="name" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Name
                </label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                  required
                />
              </div>

              {/* Email input field */}
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Email
                </label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                  required
                />
              </div>

              {/* Message textarea */}
              <div>
                <label htmlFor="message" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Message
                </label>
                <textarea
                  id="message"
                  name="message"
                  value={formData.message}
                  onChange={handleChange}
                  rows={5}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                  required
                />
              </div>

              {/* Submit button */}
              <button
                type="submit"
                className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
              >
                Send Message
              </button>
            </form>

            {/* Alternative contact methods with social links */}
            <div className="mt-8 pt-8 border-t border-gray-200 dark:border-gray-700">
              <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">
                Other Ways to Connect
              </h3>
              
              {/* Social links with optimized images */}
              <div className="mb-4">
                <ExampleSocialLinks />
              </div>
              
              {/* Traditional contact info */}
              <div className="space-y-2 text-gray-600 dark:text-gray-300">
                <p>📧 Email: your.email@example.com</p>
                <p>💼 LinkedIn: linkedin.com/in/yourprofile</p>
                <p>🐙 GitHub: github.com/yourusername</p>
                <p>🐦 Twitter: @yourhandle</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
} 