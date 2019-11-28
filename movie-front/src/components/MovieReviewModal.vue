<template>
  <v-card class="movie-review-modal" tile>
    <v-card-title>
      <span class="headline">평가하기</span>
    </v-card-title>

    <v-container fluid>
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
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        },
        body: {
          content: this.new_comment 
        }
      }

      axios.get(`http://localhost:8000/api/v1/review/comment/`, options)
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