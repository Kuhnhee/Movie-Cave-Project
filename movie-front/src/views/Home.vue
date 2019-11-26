<template>
  <div class="home">
    <MovieList :movies="movies" />
  </div>
</template>

<script>
// @ is an alias to /src
import MovieList from '@/components/MovieList.vue'
import router from '@/router'
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
    },
  },

  mounted() {
    this.loggedIn()
    this.getMovies()    
  }
}
</script>
