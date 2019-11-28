<template>
	<v-timeline
		dense
	>
		<v-timeline-item
			v-for="movie in movies"
			:key="movie.pk"
		>
			<v-card
			class="elevation-2 mx-auto"
			width="600"
			>
				<v-img
				:src="movie.img_url"
				height="150"
				>
					<v-card-title class="headline">{{ movie.title }}</v-card-title>
					<v-card-subtitle>{{ movie.open_date }}</v-card-subtitle>
				</v-img>
			</v-card>
		</v-timeline-item>
	</v-timeline>
</template>

<script>
export default {
	name: "timeline",
	data() {
		return{
			movies: sessionStorage.getItem('my_movies')
		}
	}
};
</script>

<style>
</style>