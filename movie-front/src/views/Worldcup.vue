<template>
  <v-container class="worldcup">
    <div v-if="!left">
      <v-btn white @click="next">시작</v-btn>
    </div>
    <v-row>
      <v-col cols="6">
        <WorldcupChoice id="left" :movie="left" @choiceEvent="leftChoice" />
      </v-col>
      <v-col cols="6">
        <WorldcupChoice id="right" :movie="right" @choiceEvent="rightChoice" />
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
      left: null,
      right: null,
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
        // console.log(this.current_round)
        res.data.movies.forEach(code => {
          axios.get(`http://localhost:8000/api/v1/movie/${code}/`, options)
          .then(res => {
            // console.log(res.data)
            this.current_round.push(res.data)
          })
        })
      })
    },

    leftChoice() {
      this.next_round.push(this.left)
      this.right = null
      this.next()
    },

    rightChoice() {
      this.next_round.push(this.right)
      this.right = null
      this.next()
    },

    next() {
      this.left = this.current_round.pop()
      this.right = this.current_round.pop()
    },
  },

  watch: {
    left: function() {
      if (this.current_round.length === 0 && this.left === null) {
        this.current_round = this.next_round
        this.next_round = []
      }
    }
  },


  created() {
    this.randomMovieCall()
  },
}
</script>

<style>

</style>