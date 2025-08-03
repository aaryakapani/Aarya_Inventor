/**
 * About Page Component
 * 
 * Why needed: This page provides visitors with information about you, your skills,
 * and your interests. It helps establish credibility and gives people a sense
 * of who you are professionally and personally.
 */

export default function About() {
  return (
    // Full-screen container with gradient background
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800">
      <div className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto">
          
          {/* Page title */}
          <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-8">
            About Me
          </h1>
          
          {/* Main content section */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8 mb-8">
            <h2 className="text-2xl font-semibold text-gray-800 dark:text-white mb-4">
              Welcome to my personal website! Yippee!
            </h2>
            <p className="text-gray-600 dark:text-gray-300 leading-relaxed mb-6">
              I'm passionate about technology and innovation. This website serves as a platform
              to showcase my projects, share my thoughts, and connect with like-minded individuals.
            </p>
            <p className="text-gray-600 dark:text-gray-300 leading-relaxed">
              Feel free to explore the different sections and reach out if you'd like to collaborate
              or just have a chat about technology!
            </p>
          </div>

          {/* Skills and interests grid */}
          <div className="grid md:grid-cols-2 gap-8">
            
            {/* Skills section */}
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
              <h3 className="text-xl font-semibold text-gray-800 dark:text-white mb-4">
                Skills & Technologies
              </h3>
              <ul className="space-y-2 text-gray-600 dark:text-gray-300">
                <li>• Next.js & React</li>
                <li>• TypeScript</li>
                <li>• Tailwind CSS</li>
                <li>• Node.js</li>
                <li>• Python</li>
              </ul>
            </div>

            {/* Interests section */}
            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
              <h3 className="text-xl font-semibold text-gray-800 dark:text-white mb-4">
                Interests
              </h3>
              <ul className="space-y-2 text-gray-600 dark:text-gray-300">
                <li>• Web Development</li>
                <li>• Machine Learning</li>
                <li>• IoT Projects</li>
                <li>• Open Source</li>
                <li>• Innovation</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
} 