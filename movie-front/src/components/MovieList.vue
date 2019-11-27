<template>
  <div class="movie-list">

    <v-card
      class="mx-auto"
      max-width="800"
    >
      <v-toolbar
        color="grey darken-1"
        dark
      >
        <v-toolbar-title>Movie List</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-toolbar>

      <v-container fluid v-if="movies.length">
        <v-row dense>
          <v-col
            v-for="movie in movies"
            :key="movie.id"
            :cols="col_flex"
            sm="6"
            md="3"
          >
          <v-lazy>
            <MovieCard :movie="movie"/>
          </v-lazy>
          </v-col>
        </v-row>
      </v-container>
    </v-card>

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
  },
  data() {
    return {
      col_flex: 3
    }
  },
}
</script>

<style>

</style>