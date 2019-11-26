<template>
  <div class="movie-list">
    <!-- <h2>Movie List</h2> -->
    <MovieCard/>
    <div class="card" v-for="movie in movies" :key="movie.id">
      <div class="card-body">
        <p>{{ movie.img_url }}</p>
        <img src="https://movie-phinf.pstatic.net/20130911_232/1378878991812QfLTe_JPEG/movie_image.jpg" alt="" width="100px" height="100px">
        <span>{{ movie.title }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'MovieList',
  components: {
    MovieCard,
  },
  props: {
    movies: {
      type: Array,
    }
  }
}
</script>

<style>

</style>