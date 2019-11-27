<template>
  <div id="timeline">
		<h2>Time Line</h2>
		<v-timeline
			dense
		>
			<v-timeline-item
				v-for="movie in movies"
				:key="movie.pk"
			>
				<v-card class="elevation-2">
					<div>
						<v-card-title class="headline">{{ movie.title }}</v-card-title>
						<v-card-subtitle>{{ movie.open_date }}</v-card-subtitle>
					</div>
					<v-img :src="movie.img_url"></v-img>
				</v-card>
			</v-timeline-item>
		</v-timeline>
  </div>
</template>

<script>
export default {
	name: "timeline",
	props: {
		movies: {
			type: Array
		}
	}
};
</script>

<style>
</style>