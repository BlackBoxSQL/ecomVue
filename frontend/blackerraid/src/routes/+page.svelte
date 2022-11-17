<script>
	let movies = [
		{
			name: 'Eric',
			release: '2022-02-05'
		},
		{
			name: 'Luck',
			release: '2011-05-08'
		},
	];
</script>

<svelte:head>
	<title>Blacker Raid</title>
</svelte:head>
{#each movies as movie}
	<!-- content here -->
	<p>
		{movie.name}
		{movie.release}
	</p>
{/each}

<style>
</style>
