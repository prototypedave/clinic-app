/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#C3B1E1', // Light Indigo
          DEFAULT: '#8A2BE2', // Blue Violet
          dark: '#4B0082', // Indigo
        },
        secondary: {
          light: '#E6E6FA', // Lavender (Light Violet)
          DEFAULT: '#EE82EE', // Violet
          dark: '#9400D3', // Dark Violet
        },
        white: '#FFFFFF',
      },
    },
  },
  plugins: [],
}

