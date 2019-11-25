<template>
  <div class="home">
    <MovieList :movies="movies" />
  </div>
</template>


<script>
// @ is an alias to /src
import MovieList from '@/components/MovieList'
import axios from 'axios'
import router from '@/router'
// import jwtDecode from 'jwt-decode'

export default {
  name: 'home',
  components: {
    MovieList,
  },
  data() {
    return{
      movies: []
    }
  },
  methods: {
    loggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) {
        router.push('/login')
      }
    },

    getMovies() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT' + token
        }
      }
      axios.get(`http://localhost:8000/api/v1/movies/`, options)
      .then(res => {
        this.moveis = res.data.movie_set
      })
    },

    mounted() {
      this.loggedIn(),
      this.getMovies()
    },
  },

}
</script>
