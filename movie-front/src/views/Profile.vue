<template>
  <div class="mx-auto" id="profile">
    <h2>My Page</h2>
    <div v-if="isLoggedIn">
      <Timeline :movies="movies"/>
      <ReviewList :reviews="reviews"/>
    </div>
  </div>
</template>

<script>
import Timeline from '../components/Timeline'
import ReviewList from '../components/ReviewList'
import { mapGetters } from 'vuex';
import router from '../router';
import axios from 'axios'

export default {
  name: "profile",
  data () {
    return {
      movies: [],
      reviews: [],
    }
  },
  components: {
    Timeline,
    ReviewList,
  },
  methods: {
    ...mapGetters(['isLoggedIn']),
    getInfo() {
      this.$session.start();
      const token = this.$session.get('jwt');
      const options = {
        headers: {
          Authorization: `JWT ${token}`,
        }
      };
      axios.get('http://localhost:8000/api/v1/my_movies/', options)
        .then(res => {
          this.movies = res.data.movies
          this.reviews = res.data.review_set
          })
        .catch(err => console.log(err.response));
    }
  },
  
  created () {
    router.push(this.isLoggedIn ? '/profile' : '/login');
  }
};
</script>

<style>
</style>