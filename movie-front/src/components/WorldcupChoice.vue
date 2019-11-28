<template>
  <div v-if="!!movie">
    <h2>{{movie.title}}</h2>
    <img @click="select" :src="movie.img_url" alt="" width="400px" height="600px">
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  data () {
    return {
      movieObject: null,
    }
  },
  
  props: {
    movie:{
      type: Object,
      required: false,
    }
  },

  methods: {
    select() {
      this.$emit('choiceEvent', true)
    }
  }

}
</script>

<style>

</style>