/**
 * Reusable Button Component
 * 
 * Why needed: This component provides consistent button styling across your app.
 * It supports multiple variants, sizes, and states, reducing code duplication
 * and ensuring a cohesive design system.
 */

import React from 'react';

// TypeScript interface for button props
// Why needed: TypeScript ensures proper usage and provides IntelliSense
interface ButtonProps {
  children: React.ReactNode;  // Button content (text, icons, etc.)
  onClick?: () => void;       // Click handler function
  variant?: 'primary' | 'secondary' | 'outline';  // Visual style variant
  size?: 'sm' | 'md' | 'lg';  // Size variant
  className?: string;         // Additional CSS classes
  disabled?: boolean;         // Disabled state
}

const Button: React.FC<ButtonProps> = ({
  children,
  onClick,
  variant = 'primary',  // Default to primary variant
  size = 'md',          // Default to medium size
  className = '',
  disabled = false,
}) => {
  // Base classes that apply to all buttons
  // Why needed: Ensures consistent behavior (focus states, transitions, etc.)
  const baseClasses = 'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none ring-offset-background';
  
  // Variant-specific styling classes
  // Why needed: Different visual styles for different use cases
  const variantClasses = {
    primary: 'bg-primary text-primary-foreground hover:bg-primary/90',      // Main action buttons
    secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80', // Secondary actions
    outline: 'border border-input hover:bg-accent hover:text-accent-foreground', // Subtle actions
  };
  
  // Size-specific styling classes
  // Why needed: Different sizes for different contexts and hierarchies
  const sizeClasses = {
    sm: 'h-9 px-3 text-sm',    // Small buttons for compact spaces
    md: 'h-10 py-2 px-4',      // Standard size for most use cases
    lg: 'h-11 px-8',           // Large buttons for primary actions
  };

  // Combine all classes
  const classes = `${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${className}`;

  return (
    <button
      className={classes}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
};

export default Button; 