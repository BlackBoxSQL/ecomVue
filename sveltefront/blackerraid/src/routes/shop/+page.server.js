export const load = async () => {
	const fetchMovies = async () => {
		const res = await fetch(`http://127.0.0.1:8000/api/v1/movies/`);
		const data = await res.json();
		return data.results;
	};

	return {
		movies: fetchMovies()
	};
};
