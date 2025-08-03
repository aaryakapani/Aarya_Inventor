# Setup Guide

## 🚀 Quick Start

1. **Install dependencies** (already done):
   ```bash
   npm install
   ```

2. **Start development server**:
   ```bash
   npm run dev
   ```

3. **Open your browser** and visit `http://localhost:3000`

## 📁 Project Structure

```
personal_website/
├── app/                    # Next.js App Router
│   ├── layout.tsx         # Root layout
│   ├── page.tsx           # Home page
│   ├── about/page.tsx     # About page
│   ├── contact/page.tsx   # Contact page
│   └── api/               # API routes
├── components/             # Reusable components
├── lib/                    # Utility functions
└── [config files]         # Configuration files
```

## 🎨 Customization

### 1. Update Personal Information
- Edit `app/layout.tsx` to change the site title and description
- Update `components/Navigation.tsx` to change your name
- Modify content in `app/about/page.tsx` and `app/contact/page.tsx`

### 2. Styling
- Tailwind CSS is configured and ready to use
- Edit `app/globals.css` for custom styles
- Modify `tailwind.config.ts` for theme customization

### 3. Add New Pages
- Create new folders in `app/` for new pages
- Add corresponding navigation links in `components/Navigation.tsx`

## 🔧 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

## 📦 Dependencies

- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **PostCSS** - CSS processing
- **ESLint** - Code linting

## 🌐 Deployment

### Vercel (Recommended)
1. Push your code to GitHub
2. Connect your repository to Vercel
3. Deploy automatically

### Other Platforms
- Netlify
- Railway
- DigitalOcean App Platform

## 🐛 Troubleshooting

### Common Issues

1. **Module not found errors**: Run `npm install` to install dependencies
2. **TypeScript errors**: Check `tsconfig.json` configuration
3. **Styling issues**: Ensure Tailwind CSS is properly configured

### Getting Help
- Check the [Next.js documentation](https://nextjs.org/docs)
- Review the [Tailwind CSS docs](https://tailwindcss.com/docs)
- Check the console for error messages 