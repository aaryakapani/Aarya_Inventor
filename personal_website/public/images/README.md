# Images Folder

This folder contains all the static images for your personal website.

## 📁 Folder Structure

```
public/images/
├── profile.svg          # Your profile photo (placeholder)
├── logo.png            # Your logo/branding
├── hero-bg.jpg         # Hero section background
└── icons/              # Icon files
    ├── github.svg
    └── linkedin.svg
```

## 🖼️ How to Use Images

### **1. Local Images (Recommended for Static Content)**

Place your images in this folder and reference them like this:

```jsx
import Image from 'next/image'

<Image 
  src="/images/profile.jpg" 
  alt="My profile photo"
  width={150} 
  height={150}
  className="rounded-full"
/>
```

### **2. External Images (For Social Media Avatars)**

For external images like GitHub avatars, use the `unoptimized` prop:

```jsx
<Image 
  src="https://github.com/yourusername.png" 
  alt="GitHub avatar"
  width={24} 
  height={24}
  className="rounded-full"
  unoptimized
/>
```

## 🎯 Image Optimization Benefits

**Next.js Image Component provides:**
- ✅ **Automatic format optimization** (WebP, AVIF)
- ✅ **Responsive sizing** for different screen sizes
- ✅ **Lazy loading** - images load only when needed
- ✅ **Performance** - faster page loads
- ✅ **SEO** - proper alt text and loading attributes

## 📝 Adding Your Own Images

1. **Replace the placeholder**: Replace `profile.svg` with your actual photo
2. **Add your logo**: Place your logo in this folder
3. **Update references**: Update the image paths in your components

## 🔧 Supported Formats

- **JPEG/JPG** - Best for photos
- **PNG** - Best for logos and graphics with transparency
- **SVG** - Best for icons and scalable graphics
- **WebP** - Modern format with better compression
- **AVIF** - Latest format with excellent compression

## 💡 Tips

- **Use descriptive filenames**: `profile-photo.jpg` instead of `img1.jpg`
- **Optimize before uploading**: Compress images to reduce file size
- **Use appropriate formats**: JPEG for photos, PNG for graphics, SVG for icons
- **Include alt text**: Always provide meaningful alt text for accessibility

## 🚀 Example Usage

```jsx
// Profile image
<Image 
  src="/images/profile.jpg" 
  alt="My professional headshot"
  width={200} 
  height={200}
  className="rounded-full shadow-lg"
  priority  // Load immediately for above-the-fold images
/>

// Logo
<Image 
  src="/images/logo.png" 
  alt="My personal logo"
  width={120} 
  height={40}
  className="h-10 w-auto"
/>

// Background image
<Image 
  src="/images/hero-bg.jpg" 
  alt="Hero background"
  fill
  className="object-cover"
/>
``` 