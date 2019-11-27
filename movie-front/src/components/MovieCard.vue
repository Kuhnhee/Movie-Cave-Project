<template>
  <v-hover v-slot:default="{ hover }">
    <v-card class="movie-card">

      <v-img
        :src="movie.img_url"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        height="200px"
      >
      </v-img>

        <v-expand-transition>
          <div 
            v-if="hover"
            class="d-flex transition-fast-in-fast-out black darken-2 text-center display-1 v-card--reveal"
          >
            <v-rating
              v-model="rating"
              color="orange"
              background-color="orange lighten-3"
              size="21.6"
            ></v-rating>
          </div>
        </v-expand-transition>


      <v-card-actions>

        <v-spacer></v-spacer>

        <!-- <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-bookmark</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-share-variant</v-icon>
        </v-btn> -->

        <v-dialog v-model=dialog width="600px">
          <template v-slot:activator="{ on }">
            <v-btn small v-on="on">Detail</v-btn>
          </template>
          <MovieDetailModal :movie="movie" @closeDialogEvent="closeDialog"/>
        </v-dialog>

      </v-card-actions>
    </v-card>
  </v-hover>

</template>

<script>
  import jwtDecode from 'jwt-decode'
  import MovieDetailModal from '@/components/MovieDetailModal.vue'

  export default {
    data: () => ({
      rating: 0,
      dialog: false,
    }),

    components: {
      MovieDetailModal,
    },

    props: {
      movie: {
        type: Object,
        required: false,
      }
    },

    methods: {
      getUser() {
        const token = this.$session.get('jwt')
        const user_id = jwtDecode(token).user_id
        console.log(user_id)
      },

      closeDialog(){
        this.dialog = false
      }
    },

    // watch: {
    //   rating: { //rating값이 변경될 경우 handler() 함수 실행
    //     handler(rating) {
    //       // rating이 변경될 때마다, 데이터베이스 변경을 위한 API 호출
    //       rating++
    //     },
    //     deep: true
    //   }
    // }
    
  }
</script>

<style>
.v-card--reveal {
  align-items: center;
  bottom: 20%;
  justify-content: center;
  opacity: 0.8;
  position: absolute;
}

</style>