<template>
  <v-col class="home">
    <!-- <h1>Movie List</h1> -->
    <MovieList :movies="movies"/>
  </v-col>
</template>

<script>
// @ is an alias to /src
import MovieList from '@/components/MovieList.vue'
// import router from '@/router'
import axios from 'axios'


export default {
  name: 'home',

  data () {
    return {
      movies: [],
    }
  },

  components: {
    MovieList,
  },

  methods: {
    getMovies() {
      const token = sessionStorage.getItem('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }

      axios.get('http://localhost:8000/api/v1/movie/', options)
      .then(res => {
        this.movies = res.data
      })
      .catch(error => {
        console.log(error.response)
      })

    }, // end of getMovies()
  }, // end of methods

  mounted() {
    this.getMovies()    
  }

}
</script>
