<template>
  <div>
    <h1>가입 페이지</h1>
    <SignupForm/>
  </div>
</template>

<script>
import SignupForm from '@/components/SignupForm.vue'

export default {
  name: 'Signin',
  components:{
    SignupForm,
  }
}
</script>

<style>

</style>