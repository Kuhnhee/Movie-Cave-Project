<template>
  <div>
    <h1>로그인 페이지</h1>
    <LoginForm/>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'

export default {
  name: 'Login',
  components: {
    LoginForm,
  }
}
</script>

<style>

</style>