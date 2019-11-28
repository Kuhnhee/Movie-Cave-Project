<template>
  <div class="review-list">
    <h2>Review List</h2>
    <div class="card" v-for="review in reviews" :key="review.id">
      <div class="card-body">
        <span>{{ review.content }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewList',
  props: {
    reviews: {
      type: Array,
      
    }
  }
}
</script>

<style>

</style>