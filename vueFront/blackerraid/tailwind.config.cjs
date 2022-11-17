/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#DA0606",
        secondary: "#282020",
      },
      fontFamily: {
        ibm: ["IBM Plex Sans", "sans-serif"],
      },
    },
  },
  plugins: [],
};
