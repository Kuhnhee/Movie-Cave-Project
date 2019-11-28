<template>
  <div class="mx-auto" id="profile">
    <h2>    {{ username }}'s Profile</h2>
    <v-container>
      <v-row
        justify="center"
      >
        <v-col cols="6">
          <h3>Movie Timeline</h3>
          <Timeline/>
        </v-col>
        <v-col  cols="6">
          <h3>Review List</h3>
          <ReviewList/>
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
      username: sessionStorage.getItem('username')
    }
  },

  components: {
    Timeline,
    ReviewList,
  },

  methods: {
    ...mapActions(['refreshInfo', 'refreshMovie']),
    getInfo() {
      const token = sessionStorage.getItem('jwt')
      this.refreshInfo(token)
    }
  }, 

  computed: {
    ...mapGetters(['isLoggedIn']),
  },

  created () {
    if (this.isLoggedIn) {
      this.getInfo()
    } else{
      router.push('/login')
    }
  }
};
</script>

<style>
</style>