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
        <div><b>평점</b></div>
        <div>{{ movie.rate }}</div>
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

      




    </v-container>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="green darken-1" text @click.prevent="closeDialog">닫기</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data () {
    return {
      // dialog: false,
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
    }
  }

}
</script>

<style>

</style>