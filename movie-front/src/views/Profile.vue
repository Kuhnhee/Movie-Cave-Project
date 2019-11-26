<template>
  <div class="profile">
    <h1>Profile</h1>
    <MovieList :movies="movies" />
    <ReviewList :reviews="reviews" />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import ReviewList from '@/components/ReviewList.vue'
import jwtDecode from 'jwt-decode'
import router from '@/router'
import axios from 'axios'


export default {
  name: 'profile',
  data() {
    return {
      movies: [],
      reviews: [],
    }
  },
  components: {
    ReviewList,
    MovieList,
  },
  methods: {
    loggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) {
        router.push('/login')
      }
    },

    getProfile() {
      const token = this.$session.get('jwt')
      const user_id = jwtDecode(token).user_id
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.get(`http://localhost:8000/api/v1/user/${user_id}/`, options)
      .then(res => {
        console.log(res)
        this.movies = res.data.movies
        this.reviews = res.data.review_set
      })
      .catch(error => {
        console.log(error.response)
      })
    },
  },

  mounted() {
    this.loggedIn()
    this.getProfile()
  }

}
</script>

<style>

</style>