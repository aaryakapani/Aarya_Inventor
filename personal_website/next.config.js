/**
 * Next.js Configuration File
 * 
 * Why needed: This file configures Next.js behavior, enabling modern features
 * and setting up build optimizations. In Next.js 14, the App Router is stable
 * and enabled by default, so no experimental configuration is needed.
 */

/** @type {import('next').NextConfig} */
const nextConfig = {
  // In Next.js 14, the App Router is stable and enabled by default
  // No experimental configuration needed for appDir
  
  // Image configuration for external images
  // Why needed: Allows Next.js to optimize images from external domains
  images: {
    // Domains that are allowed to serve images
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'github.com',
        port: '',
        pathname: '/**',
      },
      {
        protocol: 'https',
        hostname: 'avatars.githubusercontent.com',
        port: '',
        pathname: '/**',
      },
      {
        protocol: 'https',
        hostname: 'media.licdn.com',
        port: '',
        pathname: '/**',
      },
      {
        protocol: 'https',
        hostname: 'pbs.twimg.com',
        port: '',
        pathname: '/**',
      },
    ],
  },
}

module.exports = nextConfig 