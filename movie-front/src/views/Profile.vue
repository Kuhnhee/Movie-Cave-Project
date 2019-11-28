<template>
  <div class="mx-auto" id="profile">
    <h2>{{ username }}</h2>
    <v-container fluid>
      <v-row>
        <v-col cols="6">
          <Timeline :movies="movies"/>
        </v-col>
        <v-col  cols="6">
          <ReviewList :reviews="reviews"/>
        </v-col>
      </v-row>
    </v-container>
    
    
  </div>
</template>

<script>
import Timeline from '../components/Timeline'
import ReviewList from '../components/ReviewList'
import { mapGetters, mapActions } from 'vuex';
import router from '../router';

export default {
  name: "profile",
  
  data () {
    return {
      movies: [],
      reviews: [],
      username: sessionStorage.getItem('username')
    }
  },

  components: {
    Timeline,
    ReviewList,
  },

  methods: {
    ...mapActions(['refreshInfo']),
    getInfo() {
      const token = sessionStorage.getItem('jwt')
      this.refreshInfo(token)
      this.movies = sessionStorage.getItem('my_movies')
      this.reviews = sessionStorage.getItem('my_reviews')
    }
  }, 

  computed: {
    ...mapGetters(['isLoggedIn']),
  },

  mounted() {
    this.getInfo()
  },
  
  created () {
    router.push(this.isLoggedIn ? '/profile' : '/login')
  }
};
</script>

<style>
</style>