<template>
  <v-container class="worldcup">
    <v-row>
      <v-col cols="6">
        <WorldcupChoice id="left"/>
      </v-col>
      <v-col cols="6">
        <WorldcupChoice id="right"/>
      </v-col>
    </v-row>
    
  </v-container>
</template>

<script>
import WorldcupChoice from '@/components/WorldcupChoice.vue'
import axios from 'axios'

export default {
  data () {
    return {
      current_round: [],
      next_round: [],
      left: '',
      right: '',
    }
  },

  components: {
    WorldcupChoice,
  },
  
  methods: {
    randomMovieCall() {
      const token = sessionStorage.getItem('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.get('http://localhost:8000/api/v1/worldcup/', options)
      .then(res => {
        this.current_round = res.data.movies
        console.log(this.current_round)
      })
    }
  },

  created() {
    this.randomMovieCall()
  },

}
</script>

<style>

</style>