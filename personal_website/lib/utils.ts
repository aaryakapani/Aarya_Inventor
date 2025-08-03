/**
 * Utility Functions
 * 
 * Why needed: These utility functions provide common operations that are used
 * throughout the application, reducing code duplication and ensuring consistency.
 */

import { type ClassValue, clsx } from "clsx"  // Utility for conditional CSS classes
import { twMerge } from "tailwind-merge"      // Efficiently merges Tailwind classes

/**
 * Combines CSS classes efficiently
 * Why needed: This function intelligently merges Tailwind CSS classes,
 * preventing conflicts and ensuring proper class ordering
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

/**
 * Formats a date in a user-friendly way
 * Why needed: Provides consistent date formatting across the application
 * @param date - The date to format
 * @returns Formatted date string (e.g., "January 15, 2024")
 */
export function formatDate(date: Date): string {
  return new Intl.DateTimeFormat("en-US", {
    month: "long",    // Full month name
    day: "numeric",   // Day as number
    year: "numeric",  // Year as number
  }).format(date)
}

/**
 * Generates a unique identifier
 * Why needed: Useful for creating unique keys in lists or temporary IDs
 * @returns A random 9-character string
 */
export function generateId(): string {
  return Math.random().toString(36).substr(2, 9)
} 