<template>
  <div class="movie-list">
    <h2>Movie List</h2>
    <div class="card" v-for="movie in movies" :key="movie.id">
      <div class="card-body">
        <span>{{ movie.title }}</span>
      </div>
    </div>
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