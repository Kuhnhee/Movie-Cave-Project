<template>
  <v-simple-table fixed-header height="300px">
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">Score</th>
          <th class="text-left">Movie</th>
          <th class="text-left">Content</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="review in reviews" :key="review.pk">
          <td>{{ review.score }}</td>
          <td>{{ review.movie }}</td>
          <td>{{ review.content }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
export default {
  name: 'ReviewList',
  data() {
    return {
      reviews: sessionStorage.getItem('my_reviews')
    }
  }
}
</script>

<style>

</style>