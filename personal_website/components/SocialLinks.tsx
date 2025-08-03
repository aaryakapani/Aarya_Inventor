/**
 * Social Links Component
 * 
 * Why needed: This component demonstrates how to use Next.js Image component
 * with external images (like social media avatars) and provides a reusable
 * way to display social media links with optimized images.
 */

import Image from 'next/image'
import Link from 'next/link'

interface SocialLink {
  name: string
  url: string
  icon: string
  avatar?: string  // Optional avatar image URL
}

interface SocialLinksProps {
  links: SocialLink[]
  className?: string
}

export default function SocialLinks({ links, className = '' }: SocialLinksProps) {
  return (
    <div className={`flex flex-wrap gap-4 ${className}`}>
      {links.map((link) => (
        <Link
          key={link.name}
          href={link.url}
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center space-x-2 px-4 py-2 bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-all duration-200 hover:scale-105"
        >
          {/* Avatar image if provided */}
          {link.avatar && (
            <div className="relative">
              <Image
                src={link.avatar}
                alt={`${link.name} avatar`}
                width={24}
                height={24}
                className="rounded-full"
                // For external images, Next.js needs to know the domain
                unoptimized  // Disable optimization for external images
              />
            </div>
          )}
          
          {/* Social media icon */}
          <span className="text-2xl">{link.icon}</span>
          
          {/* Link text */}
          <span className="text-sm font-medium text-gray-700 dark:text-gray-300">
            {link.name}
          </span>
        </Link>
      ))}
    </div>
  )
}

// Example usage with sample data
export function ExampleSocialLinks() {
  const socialLinks: SocialLink[] = [
    {
      name: 'GitHub',
      url: 'https://github.com/yourusername',
      icon: '🐙',
      avatar: 'https://github.com/yourusername.png'  // GitHub avatar API
    },
    {
      name: 'LinkedIn',
      url: 'https://linkedin.com/in/yourprofile',
      icon: '💼'
    },
    {
      name: 'Twitter',
      url: 'https://twitter.com/yourhandle',
      icon: '🐦'
    },
    {
      name: 'Email',
      url: 'mailto:your.email@example.com',
      icon: '📧'
    }
  ]

  return <SocialLinks links={socialLinks} />
} 