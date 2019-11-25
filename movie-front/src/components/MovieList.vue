<template>
  <div class="container">
    <v-container v-for="movie in movies" :key="movie.id">
      <v-card
        class="mx-auto"
        max_width="400"
      >
        <v-img
          class="white--text align-end"
          height="200px"
          src="movie.img_url"
        >
          <v-card-title>{{ movie.title }}</v-card-title>
        </v-img>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'MovieList',
  props: {
    movies: {
      type: Array,
    }
  }
}
</script>

<style>

</style>