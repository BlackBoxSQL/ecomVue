/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				primary: '#DA0606',
				secondary: '#282020'
			},
			fontFamily: {
				ibm: ["IBM Plex Sans", 'sans-serif'],
			},
		}
	},
	plugins: []
};
