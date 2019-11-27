<template>

  <v-card class="movie-detail-modal" tile>
    <v-card-title>
      <span class="headline">{{ movie.title }}</span>
      <span v-if="movie.title_en">({{ movie.title_en }})</span>
    </v-card-title>

    
    <v-container fluid>

      <v-divider></v-divider>
      <v-row justify="space-around">
        <v-col cols="5">
          <v-img
            :src="movie.img_url"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
          >
          </v-img>
        </v-col>
      </v-row>

      <v-divider></v-divider>

      <v-card-text>
        <div><b>감독</b> | <span v-for="name in directors" :key=name>{{ name }}, </span></div>
        <div><b>배우</b> | <span v-for="name in actors" :key=name>{{ name }}, </span></div>
        <div><b>평점</b> | <span>{{ movie.rate }}</span></div>
      </v-card-text>

      <v-divider></v-divider>

      <v-expansion-panels accordion>
        <v-expansion-panel accordion>
          <v-expansion-panel-header>줄거리</v-expansion-panel-header>
          <v-expansion-panel-content>
            {{ movie.description }}
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
      
      <v-divider></v-divider>

      <v-row>
        <v-col cols="9">
          <v-text-field label="댓글" v-model="new_comment"></v-text-field>
        </v-col>
        <v-col cols="3" class="mt-3">
          <v-btn @click="writeComment">
            <v-icon>mdi-pencil</v-icon>입력하기
          </v-btn>
        </v-col>

      </v-row>
      

    </v-container>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="green darken-1" text @click.prevent="closeDialog">닫기</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      directors: [],
      actors: [],
      new_comment: '',
    }
  },

  props: {
    movie: {
      type: Object,
      required: false,
    }
  },

  methods: {
    closeDialog() {
      this.$emit('closeDialogEvent', true)
    },

    directorsNameCall() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      this.movie.directors.forEach(code => {
        axios.get(`http://localhost:8000/api/v1/director/${code}/`, options)
        .then(res => {
          this.directors.push(res.data.name)
        })
        .catch(error => {
          console.log(error.response)
        })
      })
    },

    actorsNameCall() {
      const token = this.$session.get('jwt')
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      this.movie.actors.forEach(code => {
        axios.get(`http://localhost:8000/api/v1/actor/${code}/`, options)
        .then(res => {
          this.actors.push(res.data.name)
        })
        .catch(error => {
          console.log(error.response)
        })
      })
    },

    writeComment() {
      const token = this.$session.get('jwt')
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

  }, //end of methods

  mounted() {
    this.directorsNameCall()
    this.actorsNameCall()
  }
}
</script>

<style>

</style>