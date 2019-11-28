<template>
  <v-card class="movie-review-modal" tile>
    <v-card-title>
      <span class="headline">평가하기</span>
    </v-card-title>

    <v-container fluid>

      <div class="text-center">
        <v-rating
          readonly
          v-model="rating"
          color="orange"
          background-color="orange lighten-3"
          size="21.6"
        ></v-rating>
      </div>

      <v-row>
        <v-col cols="9">
          <v-text-field label="코멘트" v-model="new_comment"></v-text-field>
        </v-col>
        <v-col cols="3" class="mt-3">
          <v-btn @click="writeComment" @click.prevent="closeDialog">
            <v-icon>mdi-pencil</v-icon>입력하기
          </v-btn>
        </v-col>
      </v-row>

    </v-container>

  </v-card>
  
</template>

<script>
import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  data () {
    return {
      new_comment: '',
    }
  },

  props: {
    movie: {
      type: Object,
      required: false,
    },
    rating: {
      type: Number,
      required: false,
    }
  },

  methods: {
    closeDialog() {
      this.$emit('closeDialogEvent', true)
    },

    writeComment() {
      const token = sessionStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      console.log(token)

      const headers = {'Authorization': `JWT ${token}`}
      const review = {
        'content': this.new_comment,
        'scoore': this.rating,
        'movie': this.movie.id,
        'user': user_id
      }

      axios.post('http://localhost:8000/api/v1/review/', review, headers)
      .then(res => {
        console.log(res)
      })
      .catch(error => {
        console.log(error.response)
      })
    }

  },

}
</script>

<style>

</style>